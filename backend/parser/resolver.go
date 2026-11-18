package parser

import (
	"context"
	"fmt"
	"math"
	"sync"
	"time"
)

// CountryMeta метаданные страны
type CountryMeta struct {
	Code      string
	Name      string
	Currency  string
	Symbol    string
	VatRate   float64 // Налог на цифровые услуги
	PPPFactor float64 // Относительный индекс покупательской способности для цифровых сервисов
}

var DefaultCountriesMeta = map[string]CountryMeta{
	"US": {Code: "US", Name: "United States", Currency: "USD", Symbol: "$", VatRate: 0.0, PPPFactor: 1.0},
	"TR": {Code: "TR", Name: "Turkey", Currency: "TRY", Symbol: "₺", VatRate: 0.20, PPPFactor: 0.25},
	"NG": {Code: "NG", Name: "Nigeria", Currency: "NGN", Symbol: "₦", VatRate: 0.075, PPPFactor: 0.18},
	"AR": {Code: "AR", Name: "Argentina", Currency: "ARS", Symbol: "$", VatRate: 0.59, PPPFactor: 0.28},
	"IN": {Code: "IN", Name: "India", Currency: "INR", Symbol: "₹", VatRate: 0.18, PPPFactor: 0.22},
	"KZ": {Code: "KZ", Name: "Kazakhstan", Currency: "KZT", Symbol: "₸", VatRate: 0.12, PPPFactor: 0.45},
	"UA": {Code: "UA", Name: "Ukraine", Currency: "UAH", Symbol: "₴", VatRate: 0.20, PPPFactor: 0.35},
	"BR": {Code: "BR", Name: "Brazil", Currency: "BRL", Symbol: "R$", VatRate: 0.0925, PPPFactor: 0.38},
	"PL": {Code: "PL", Name: "Poland", Currency: "PLN", Symbol: "zł", VatRate: 0.23, PPPFactor: 0.55},
	"EU": {Code: "EU", Name: "Eurozone", Currency: "EUR", Symbol: "€", VatRate: 0.21, PPPFactor: 1.05},
	"GB": {Code: "GB", Name: "United Kingdom", Currency: "GBP", Symbol: "£", VatRate: 0.20, PPPFactor: 1.15},
	"EG": {Code: "EG", Name: "Egypt", Currency: "EGP", Symbol: "E£", VatRate: 0.14, PPPFactor: 0.22},
	"PH": {Code: "PH", Name: "Philippines", Currency: "PHP", Symbol: "₱", VatRate: 0.12, PPPFactor: 0.30},
	"JP": {Code: "JP", Name: "Japan", Currency: "JPY", Symbol: "¥", VatRate: 0.10, PPPFactor: 0.85},
	"RU": {Code: "RU", Name: "Russia", Currency: "RUB", Symbol: "₽", VatRate: 0.20, PPPFactor: 0.30},
}

// Resolver управляет цепочкой источников
type Resolver struct {
	adapters      map[string]ServiceAdapter
	rates         map[string]float64 // сколько USD стоит 1 единица валюты
	communityDB   map[string]map[string]PriceResult // service -> country -> price
	archiveDB     map[string]map[string]PriceResult // service -> country -> price
	cache         sync.Map                          // key: "service:plan:country" -> *PriceResult
	cacheTTL      time.Duration
}

func NewResolver(rates map[string]float64) *Resolver {
	if rates == nil {
		rates = make(map[string]float64)
	}
	r := &Resolver{
		adapters:    make(map[string]ServiceAdapter),
		rates:       rates,
		communityDB: make(map[string]map[string]PriceResult),
		archiveDB:   make(map[string]map[string]PriceResult),
		cacheTTL:    24 * time.Hour,
	}
	r.initKnowledgeBases()
	return r
}

func (r *Resolver) RegisterAdapter(a ServiceAdapter) {
	r.adapters[a.ID()] = a
}

// ConvertToUSD конвертирует сумму в USD
func (r *Resolver) ConvertToUSD(amount float64, currency string) float64 {
	rate, ok := r.rates[currency]
	if !ok || rate <= 0 {
		return amount
	}
	return amount * rate
}

// ConvertFromUSD конвертирует USD в местную валюту
func (r *Resolver) ConvertFromUSD(usdAmount float64, targetCurrency string) float64 {
	rate, ok := r.rates[targetCurrency]
	if !ok || rate <= 0 {
		return usdAmount
	}
	return usdAmount / rate
}

// Resolve выполняет поиск цены строго по 6-уровневой цепочке источников
func (r *Resolver) Resolve(ctx context.Context, serviceID, planID, countryCode string, baseUSPrice float64) (*PriceResult, error) {
	cacheKey := fmt.Sprintf("%s:%s:%s", serviceID, planID, countryCode)
	if val, ok := r.cache.Load(cacheKey); ok {
		cached := val.(*PriceResult)
		if time.Since(cached.FetchedAt) < r.cacheTTL {
			return cached, nil
		}
	}

	adapter := r.adapters[serviceID]
	cMeta, ok := DefaultCountriesMeta[countryCode]
	if !ok {
		cMeta = CountryMeta{Code: countryCode, Currency: "USD", Symbol: "$", VatRate: 0.0, PPPFactor: 1.0}
	}

	var result *PriceResult
	var lastErr error

	// ==================== 1. OFFICIAL ====================
	if adapter != nil {
		res, err := adapter.FetchOfficial(ctx, planID, countryCode)
		if err == nil && res != nil && res.Amount > 0 {
			res.Source = SourceOfficial
			if res.SourceURL == "" {
				res.SourceURL = fmt.Sprintf("https://www.%s.com/%s/pricing", serviceID, countryCode)
			}
			if res.SourceDate == "" {
				res.SourceDate = time.Now().Format("2006-01-02")
			}
			result = res
		} else if err != nil {
			lastErr = err
		}
	}

	// ==================== 2. STORE ====================
	if result == nil && adapter != nil {
		res, err := adapter.FetchStore(ctx, planID, countryCode)
		if err == nil && res != nil && res.Amount > 0 {
			res.Source = SourceStore
			if res.SourceDate == "" {
				res.SourceDate = time.Now().Format("2006-01-02")
			}
			result = res
		} else if err != nil {
			lastErr = err
		}
	}

	// ==================== 3. USD_FLAT ====================
	// Сервис продает по единой цене в USD (или адаптер явно помечен IsGlobalUSD)
	if result == nil && (adapter != nil && adapter.IsGlobalUSD()) {
		taxMultiplier := 1.0
		includesTax := false
		if countryCode == "EU" || countryCode == "PL" || countryCode == "GB" {
			taxMultiplier = 1.0 + cMeta.VatRate
			includesTax = true
		}
		
		finalAmount := math.Round(baseUSPrice*taxMultiplier*100) / 100
		curr := "USD"
		if countryCode == "EU" {
			curr = "EUR"
			finalAmount = r.ConvertFromUSD(baseUSPrice*taxMultiplier, "EUR")
		} else if countryCode == "GB" {
			curr = "GBP"
			finalAmount = r.ConvertFromUSD(baseUSPrice*taxMultiplier, "GBP")
		}

		status := "global_usd"
		available := true
		if countryCode == "RU" {
			status = "suspended"
			available = false
		}

		result = &PriceResult{
			Amount:            finalAmount,
			Currency:          curr,
			Period:            "month",
			IncludesTax:       includesTax,
			Source:            SourceUSDFlat,
			SourceURL:         fmt.Sprintf("https://www.%s.com/pricing", serviceID),
			SourceDate:        time.Now().Format("2006-01-02"),
			Available:         available,
			Status:            status,
			StatusLabel:       "Global $",
			PaymentDifficulty: "medium",
			PaymentNotes:      "Единый глобальный тариф в USD. Для оплаты подходят зарубежные карты.",
		}
	}

	// ==================== 4. COMMUNITY ====================
	if result == nil {
		if sMap, ok := r.communityDB[serviceID]; ok {
			if commPrice, ok := sMap[countryCode]; ok && commPrice.Amount > 0 {
				cp := commPrice
				cp.Source = SourceCommunity
				result = &cp
			}
		}
	}

	// ==================== 5. ARCHIVE ====================
	if result == nil {
		if aMap, ok := r.archiveDB[serviceID]; ok {
			if archPrice, ok := aMap[countryCode]; ok && archPrice.Amount > 0 {
				ap := archPrice
				ap.Source = SourceArchive
				result = &ap
			}
		}
	}

	// ==================== 6. ESTIMATED ====================
	if result == nil {
		// Расчетная оценка: базовый US прайс * PPPFactor страны, конвертированный в валюту страны
		estUSD := math.Round(baseUSPrice*cMeta.PPPFactor*100) / 100
		if estUSD <= 0 {
			estUSD = baseUSPrice
		}
		estLocal := r.ConvertFromUSD(estUSD, cMeta.Currency)
		
		// Округление под стандарт ценников страны
		estLocal = roundLocalPrice(estLocal, cMeta.Currency)

		status := "available"
		available := true
		if countryCode == "RU" {
			status = "suspended"
			available = false
		}

		result = &PriceResult{
			Amount:            estLocal,
			Currency:          cMeta.Currency,
			Period:            "month",
			IncludesTax:       true,
			Source:            SourceEstimated,
			SourceURL:         "https://data.worldbank.org/indicator/PA.NUS.PRPC.PP",
			SourceDate:        "2026-01-01",
			Available:         available,
			Status:            status,
			StatusLabel:       "Оценка (PPP)",
			PaymentDifficulty: "hard",
			PaymentNotes:      "Расчетная стоимость на основе регионального уровня доходов (PPP)",
		}
	}

	if result == nil {
		return nil, fmt.Errorf("failed to resolve price for %s in %s: %w", serviceID, countryCode, lastErr)
	}

	result.FetchedAt = time.Now()

	// ==================== ПРОВЕРКА НА ВЫБРОСЫ (> 5X) ====================
	if baseUSPrice > 0 {
		usdValue := r.ConvertToUSD(result.Amount, result.Currency)
		if usdValue > 5.0*baseUSPrice || (usdValue < 0.20*baseUSPrice && usdValue > 0) {
			result.NeedsReview = true
		}
	}

	r.cache.Store(cacheKey, result)
	return result, nil
}

// roundLocalPrice округляет цену в соответствии с правилами ритейла валюты
func roundLocalPrice(val float64, currency string) float64 {
	switch currency {
	case "TRY", "PLN", "BRL", "EGP", "PHP":
		// Округление до .99
		intPart := math.Floor(val)
		if intPart <= 0 {
			intPart = 1
		}
		return intPart + 0.99
	case "ARS", "NGN", "INR", "KZT", "JPY", "RUB":
		// Округление до круглых сотен/десятков
		if val > 1000 {
			return math.Round(val/100) * 100
		}
		return math.Round(val/10) * 10
	default:
		return math.Round(val*100) / 100
	}
}
