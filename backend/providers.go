package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"math"
	"math/rand"
	"net/http"
	"net/http/cookiejar"
	"net/url"
	"os"
	"strings"
	"sync"
	"time"
)

// ==================== КУРСЫ ВАЛЮТ (open.er-api.com) ====================

type RatesResponse struct {
	Result string             `json:"result"`
	Rates  map[string]float64 `json:"rates"`
}

var (
	ratesMutex sync.RWMutex
	lastRatesFetch time.Time
)

// Обновляет глобальные курсы валют с open.er-api.com
func UpdateLiveExchangeRates() error {
	client := &http.Client{Timeout: 8 * time.Second}
	resp, err := client.Get("https://open.er-api.com/v6/latest/USD")
	if err != nil {
		return fmt.Errorf("failed to fetch live exchange rates: %w", err)
	}
	defer resp.Body.Close()

	var data RatesResponse
	if err := json.NewDecoder(resp.Body).Decode(&data); err != nil {
		return err
	}

	if data.Result != "success" || len(data.Rates) == 0 {
		return fmt.Errorf("invalid rates response")
	}

	ratesMutex.Lock()
	defer ratesMutex.Unlock()

	// data.Rates["TRY"] = количество лир за 1 USD (например 34.5)
	// В нашей модели SupportedCurrencies[code] = сколько USD стоит 1 единица валюты
	// Значит SupportedCurrencies[code] = 1.0 / rate
	for code, ratePerUSD := range data.Rates {
		if ratePerUSD > 0 {
			SupportedCurrencies[code] = 1.0 / ratePerUSD
		}
	}
	SupportedCurrencies["USD"] = 1.0
	lastRatesFetch = time.Now()
	log.Printf("✅ Live exchange rates updated from open.er-api.com (%d currencies)", len(data.Rates))
	return nil
}

// ==================== MICROSOFT STORE PROVIDER ====================

type MSStoreProvider struct {
	client *http.Client
}

func NewMSStoreProvider() *MSStoreProvider {
	return &MSStoreProvider{
		client: &http.Client{Timeout: 10 * time.Second},
	}
}

func (p *MSStoreProvider) Fetch(ctx context.Context, plan PlanRef, market string) (Price, error) {
	if plan.MSBigID == "" {
		return Price{}, fmt.Errorf("missing MSBigID")
	}

	u := fmt.Sprintf(
		"https://displaycatalog.mp.microsoft.com/v7.0/products?bigIds=%s&market=%s&languages=en-US",
		plan.MSBigID, market,
	)

	req, err := http.NewRequestWithContext(ctx, "GET", u, nil)
	if err != nil {
		return Price{}, err
	}
	req.Header.Set("User-Agent", "SubDB-Monitor/1.0 (+https://subdb.info)")

	resp, err := p.client.Do(req)
	if err != nil {
		return Price{}, err
	}
	defer resp.Body.Close()

	if resp.StatusCode == 404 {
		return Price{Status: "not_available"}, ErrNotAvailable
	}

	var r struct {
		Products []struct {
			DisplaySkuAvailabilities []struct {
				Availabilities []struct {
					Actions             []string `json:"Actions"`
					OrderManagementData struct {
						Price struct {
							ListPrice     float64 `json:"ListPrice"`
							CurrencyCode  string  `json:"CurrencyCode"`
							IsTaxIncluded bool    `json:"IsTaxIncluded"`
						} `json:"Price"`
					} `json:"OrderManagementData"`
				} `json:"Availabilities"`
			} `json:"DisplaySkuAvailabilities"`
		} `json:"Products"`
	}

	if err := json.NewDecoder(resp.Body).Decode(&r); err != nil {
		return Price{}, err
	}

	if len(r.Products) == 0 {
		return Price{Status: "not_available"}, ErrNotAvailable
	}

	// Ищем актуальную месячную цену среди Availabilities
	var bestPrice float64 = 0
	var currencyCode string
	var taxIncluded bool

	for _, sku := range r.Products[0].DisplaySkuAvailabilities {
		for _, a := range sku.Availabilities {
			p := a.OrderManagementData.Price
			if p.ListPrice > 0 {
				if bestPrice == 0 || p.ListPrice < bestPrice {
					bestPrice = p.ListPrice
					currencyCode = p.CurrencyCode
					taxIncluded = p.IsTaxIncluded
				}
			}
		}
	}

	if bestPrice == 0 {
		return Price{Status: "not_available"}, ErrNotAvailable
	}

	status := "available"
	if market != "US" && currencyCode == "USD" {
		status = "global_usd"
	}

	return Price{
		Amount:    bestPrice,
		Currency:  currencyCode,
		InclTax:   taxIncluded,
		Source:    "Microsoft Store Official API",
		FetchedAt: time.Now(),
		Status:    status,
	}, nil
}

// ==================== STEAM STORE PROVIDER ====================

type SteamProvider struct {
	client *http.Client
}

func NewSteamProvider() *SteamProvider {
	return &SteamProvider{
		client: &http.Client{Timeout: 10 * time.Second},
	}
}

func (p *SteamProvider) Fetch(ctx context.Context, plan PlanRef, cc string) (Price, error) {
	if plan.SteamAppID == 0 {
		return Price{}, fmt.Errorf("missing SteamAppID")
	}

	u := fmt.Sprintf(
		"https://store.steampowered.com/api/appdetails?appids=%d&cc=%s",
		plan.SteamAppID, cc,
	)

	req, err := http.NewRequestWithContext(ctx, "GET", u, nil)
	if err != nil {
		return Price{}, err
	}
	req.Header.Set("User-Agent", "SubDB-Monitor/1.0 (+https://subdb.info)")

	resp, err := p.client.Do(req)
	if err != nil {
		return Price{}, err
	}
	defer resp.Body.Close()

	var res map[string]struct {
		Success bool `json:"success"`
		Data    struct {
			PriceOverview struct {
				Currency string  `json:"currency"`
				Initial  float64 `json:"initial"`
				Final    float64 `json:"final"`
			} `json:"price_overview"`
		} `json:"data"`
	}

	if err := json.NewDecoder(resp.Body).Decode(&res); err != nil {
		return Price{}, err
	}

	appKey := fmt.Sprintf("%d", plan.SteamAppID)
	item, ok := res[appKey]
	if !ok || !item.Success {
		return Price{Status: "not_available"}, ErrNotAvailable
	}

	po := item.Data.PriceOverview
	if po.Final == 0 {
		return Price{Status: "not_available"}, ErrNotAvailable
	}

	// Steam возвращает цену в центах/тиынах/копейках -> делим на 100
	amount := po.Final / 100.0

	status := "available"
	if cc != "US" && po.Currency == "USD" {
		status = "global_usd"
	}

	return Price{
		Amount:    amount,
		Currency:  po.Currency,
		InclTax:   true,
		Source:    "Steam Store Official API",
		FetchedAt: time.Now(),
		Status:    status,
	}, nil
}

// ==================== РЕГИОНАЛЬНЫЙ ПУЛ КЛИЕНТОВ (GEOIP & PROXY) ====================

// RegionalClientManager обеспечивает строгую изоляцию CookieJar, HTTP Transport, прокси и заголовков Accept-Language по странам
type RegionalClientManager struct {
	mu      sync.RWMutex
	clients map[string]*http.Client
}

var GlobalRegionalClients = NewRegionalClientManager()

func NewRegionalClientManager() *RegionalClientManager {
	return &RegionalClientManager{
		clients: make(map[string]*http.Client),
	}
}

// GetClient возвращает изолированный http.Client для заданной страны
func (m *RegionalClientManager) GetClient(countryCode string) *http.Client {
	cc := strings.ToUpper(countryCode)
	m.mu.RLock()
	c, exists := m.clients[cc]
	m.mu.RUnlock()
	if exists {
		return c
	}

	m.mu.Lock()
	defer m.mu.Unlock()

	// Двойная проверка
	if c, exists := m.clients[cc]; exists {
		return c
	}

	// Изолированный CookieJar для страны
	jar, _ := cookiejar.New(nil)

	transport := &http.Transport{
		MaxIdleConns:        20,
		IdleConnTimeout:     30 * time.Second,
		DisableCompression: false,
	}

	// Поддержка прокси:
	// 1) SUBS4R_PROXY_TR, SUBS4R_PROXY_UA, SUBS4R_PROXY_AR ...
	// 2) Шаблон SUBS4R_PROXY_TEMPLATE (например: "http://127.0.0.1:108%02d" для Sing-Box/Mihomo)
	envKey := fmt.Sprintf("SUBS4R_PROXY_%s", cc)
	proxyURLStr := os.Getenv(envKey)
	if proxyURLStr != "" {
		if u, err := url.Parse(proxyURLStr); err == nil {
			transport.Proxy = http.ProxyURL(u)
			log.Printf("🌐 [Proxy] Regional client [%s] mapped to proxy: %s", cc, u.Host)
		}
	}

	client := &http.Client{
		Transport: transport,
		Jar:       jar,
		Timeout:   15 * time.Second,
	}

	m.clients[cc] = client
	return client
}

// RegionalAcceptLanguage возвращает аутентичный заголовок Accept-Language для страны
func RegionalAcceptLanguage(cc string) string {
	switch strings.ToUpper(cc) {
	case "TR":
		return "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
	case "UA":
		return "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7"
	case "AR":
		return "es-AR,es;q=0.9,en-US;q=0.8,en;q=0.7"
	case "KZ":
		return "kk-KZ,ru-RU;q=0.9,en;q=0.7"
	case "IN":
		return "en-IN,en;q=0.9,hi;q=0.8"
	case "NG":
		return "en-NG,en;q=0.9"
	case "PL":
		return "pl-PL,pl;q=0.9,en-US;q=0.8"
	case "BR":
		return "pt-BR,pt;q=0.9,en-US;q=0.8"
	case "EG":
		return "ar-EG,ar;q=0.9,en-US;q=0.8"
	case "JP":
		return "ja-JP,ja;q=0.9,en-US;q=0.8"
	case "RU":
		return "ru-RU,ru;q=0.9,en-US;q=0.8"
	default:
		return "en-US,en;q=0.9"
	}
}

// ApplyJitter делает паузу между запросами к одному домену, чтобы не ловить 429
func ApplyJitter(minSec, maxSec int) {
	if minSec <= 0 {
		minSec = 2
	}
	if maxSec <= minSec {
		maxSec = minSec + 3
	}
	diff := maxSec - minSec
	d := time.Duration(minSec*1000+rand.Intn(diff*1000)) * time.Millisecond
	time.Sleep(d)
}

// ==================== APPLE APP STORE PROVIDER ====================

type AppleStoreProvider struct {
	clientMgr *RegionalClientManager
}

func NewAppleStoreProvider() *AppleStoreProvider {
	return &AppleStoreProvider{
		clientMgr: GlobalRegionalClients,
	}
}

func (p *AppleStoreProvider) Fetch(ctx context.Context, plan PlanRef, country string) (Price, error) {
	if plan.AppleAppID == 0 {
		return Price{}, fmt.Errorf("missing AppleAppID")
	}

	cc := strings.ToLower(country)
	client := p.clientMgr.GetClient(country)

	// 1. Публичный JSON lookup API: https://itunes.apple.com/lookup?id=...&country=...
	lookupURL := fmt.Sprintf("https://itunes.apple.com/lookup?id=%d&country=%s", plan.AppleAppID, cc)
	req, err := http.NewRequestWithContext(ctx, "GET", lookupURL, nil)
	if err != nil {
		return Price{}, err
	}
	req.Header.Set("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
	req.Header.Set("Accept-Language", RegionalAcceptLanguage(country))

	resp, err := client.Do(req)
	if err != nil {
		return Price{}, err
	}
	defer resp.Body.Close()

	if resp.StatusCode == 429 || resp.StatusCode == 403 {
		return Price{}, fmt.Errorf("rate limited by Apple (HTTP %d)", resp.StatusCode)
	}

	var data struct {
		ResultCount int `json:"resultCount"`
		Results     []struct {
			TrackID        int64   `json:"trackId"`
			Currency       string  `json:"currency"`
			Price          float64 `json:"price"`
			FormattedPrice string  `json:"formattedPrice"`
		} `json:"results"`
	}

	if err := json.NewDecoder(resp.Body).Decode(&data); err != nil {
		return Price{}, err
	}

	if data.ResultCount == 0 || len(data.Results) == 0 {
		return Price{Status: "not_available"}, ErrNotAvailable
	}

	result := data.Results[0]
	curr := result.Currency
	if curr == "" {
		curr = "USD"
	}

	status := "available"
	if strings.ToUpper(country) != "US" && curr == "USD" {
		status = "global_usd"
	}

	return Price{
		Amount:    result.Price,
		Currency:  curr,
		InclTax:   true,
		Source:    "Apple App Store Lookup API",
		FetchedAt: time.Now(),
		Status:    status,
	}, nil
}

// ==================== ПЛАНИРОВЩИК & ЗАЩИТА ОТ МУСОРА ====================

type SyncScheduler struct {
	msStore    *MSStoreProvider
	steam      *SteamProvider
	appleStore *AppleStoreProvider
}

func NewSyncScheduler() *SyncScheduler {
	return &SyncScheduler{
		msStore:    NewMSStoreProvider(),
		steam:      NewSteamProvider(),
		appleStore: NewAppleStoreProvider(),
	}
}

// Применяет полученную цену к базе с защитой от мусора
func applyPriceUpdate(serviceID, planID, countryCode string, price Price) {
	rawServicesMutex.Lock()
	defer rawServicesMutex.Unlock()

	for sIdx := range RawServicesData {
		s := &RawServicesData[sIdx]
		if s.ID != serviceID {
			continue
		}

		for pIdx := range s.Plans {
			plan := &s.Plans[pIdx]
			if plan.ID != planID {
				continue
			}

			// Ищем существующую цену для страны
			var foundPrice *PlanPrice
			for priceIdx := range plan.Prices {
				if plan.Prices[priceIdx].CountryCode == countryCode {
					foundPrice = &plan.Prices[priceIdx]
					break
				}
			}

			if foundPrice != nil {
				// ПРОВЕРКА НА АДЕКВАТНОСТЬ (> 30% изменение)
				if foundPrice.OriginalPrice > 0 && price.Amount > 0 {
					ratio := math.Abs(price.Amount-foundPrice.OriginalPrice) / foundPrice.OriginalPrice
					if ratio > 0.30 {
						log.Printf("⚠️ [NeedsReview] Service %s Country %s price changed by %.1f%% (old: %.2f %s, new: %.2f %s)",
							serviceID, countryCode, ratio*100, foundPrice.OriginalPrice, foundPrice.Currency, price.Amount, price.Currency)
						foundPrice.NeedsReview = true
						// Не затираем старую цену моментально, помечаем на проверку
						foundPrice.FetchedAt = price.FetchedAt.Format("2006-01-02 15:04")
						return
					}
				}

				// Если цена изменилась -> добавляем в PriceHistory
				if foundPrice.OriginalPrice != price.Amount && price.Amount > 0 {
					rate := SupportedCurrencies[price.Currency]
					if rate == 0 {
						rate = 1.0
					}
					newUSD := math.Round(price.Amount*rate*100) / 100
					foundPrice.PriceHistory = append(foundPrice.PriceHistory, newUSD)
					if len(foundPrice.PriceHistory) > 12 {
						foundPrice.PriceHistory = foundPrice.PriceHistory[1:]
					}
				}

				foundPrice.OriginalPrice = price.Amount
				foundPrice.Currency = price.Currency
				foundPrice.Symbol = CurrencySymbols[price.Currency]
				foundPrice.Status = price.Status
				foundPrice.InclTax = price.InclTax
				foundPrice.Source = price.Source
				foundPrice.FetchedAt = price.FetchedAt.Format("2006-01-02 15:04")
				foundPrice.NeedsReview = false

				// Человекочитаемый лейбл
				switch price.Status {
				case "not_available":
					foundPrice.StatusLabel = "Не запущен"
				case "global_usd":
					foundPrice.StatusLabel = "Global $"
				case "suspended":
					foundPrice.StatusLabel = "Приостановлен"
				default:
					foundPrice.StatusLabel = "Доступен"
				}
				return
			}
		}
	}
}

// Запускает синхронизацию для провайдеров
func (s *SyncScheduler) RunSync(ctx context.Context) {
	log.Println("🔄 Starting pricing provider sync cycle...")

	// 1. Обновляем курсы валют
	if err := UpdateLiveExchangeRates(); err != nil {
		log.Printf("Rates update warning: %v", err)
	}

	// 2. Синхронизируем Xbox Game Pass Ultimate через MS Store API
	gamePassMarkets := []string{"TR", "IN", "BR", "PL", "US", "KZ", "UA"}
	for _, market := range gamePassMarkets {
		p, err := s.msStore.Fetch(ctx, PlanRef{
			ServiceID: "xbox-game-pass",
			PlanID:    "ultimate",
			MSBigID:   "CFQ7TTC0KHS0",
		}, market)

		if err != nil {
			log.Printf("MS Store [%s]: %v", market, err)
			continue
		}
		applyPriceUpdate("xbox-game-pass", "ultimate", market, p)
		time.Sleep(300 * time.Millisecond) // rate limiter
	}

	// 3. Синхронизируем Steam EA Play через Steam API
	steamMarkets := []string{"KZ", "UA", "TR", "US", "PL"}
	for _, cc := range steamMarkets {
		p, err := s.steam.Fetch(ctx, PlanRef{
			ServiceID:  "steam-ea-play",
			PlanID:     "monthly",
			SteamAppID: 1289670,
		}, cc)

		if err != nil {
			log.Printf("Steam [%s]: %v", cc, err)
			continue
		}
		applyPriceUpdate("steam-ea-play", "monthly", cc, p)
		time.Sleep(400 * time.Millisecond) // rate limiter
	}

	log.Println("✅ Pricing provider sync cycle completed.")
}
