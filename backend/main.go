package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"math"
	"net/http"
	"os"
	"sort"
	"strings"
	"sync"
	"time"
)

var (
	rawServicesMutex sync.RWMutex
	suggestionsLock  sync.Mutex
	savedSuggestions []SuggestionRequest
	scheduler        *SyncScheduler
)

// Helper: конвертирует цену из одной валюты в другую через USD
func convertCurrency(amount float64, fromCur, toCur string) float64 {
	ratesMutex.RLock()
	fromRate, ok1 := SupportedCurrencies[fromCur]
	if !ok1 {
		fromRate = 1.0
	}
	toRate, ok2 := SupportedCurrencies[toCur]
	if !ok2 {
		toRate = 1.0
	}
	ratesMutex.RUnlock()

	// amount in USD:
	usd := amount * fromRate
	// to target currency:
	target := usd / toRate
	return math.Round(target*100) / 100
}

func corsMiddleware(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Access-Control-Allow-Origin", "*")
		w.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
		w.Header().Set("Access-Control-Allow-Headers", "Content-Type, Authorization")
		w.Header().Set("Content-Type", "application/json; charset=utf-8")

		if r.Method == http.MethodOptions {
			w.WriteHeader(http.StatusOK)
			return
		}
		next(w, r)
	}
}

func handleHealth(w http.ResponseWriter, r *http.Request) {
	ratesMutex.RLock()
	ratesCount := len(SupportedCurrencies)
	lastRates := lastRatesFetch.Format(time.RFC3339)
	ratesMutex.RUnlock()

	json.NewEncoder(w).Encode(map[string]interface{}{
		"status":          "ok",
		"service":         "SubDB Go Backend",
		"version":         "2.0.0",
		"currencies_count": ratesCount,
		"last_rates_sync": lastRates,
	})
}

func handleCurrencies(w http.ResponseWriter, r *http.Request) {
	type CurInfo struct {
		Code    string  `json:"code"`
		Symbol  string  `json:"symbol"`
		RateUSD float64 `json:"rate_usd"`
	}
	var list []CurInfo
	ratesMutex.RLock()
	for code, rate := range SupportedCurrencies {
		list = append(list, CurInfo{
			Code:    code,
			Symbol:  CurrencySymbols[code],
			RateUSD: rate,
		})
	}
	ratesMutex.RUnlock()

	sort.Slice(list, func(i, j int) bool {
		return list[i].Code < list[j].Code
	})
	json.NewEncoder(w).Encode(list)
}

func handleCountries(w http.ResponseWriter, r *http.Request) {
	json.NewEncoder(w).Encode(AllCountries)
}

func computeServiceSummaries(targetCurrency string) []ServiceSummary {
	rawServicesMutex.RLock()
	defer rawServicesMutex.RUnlock()

	var summaries []ServiceSummary

	for _, s := range RawServicesData {
		summary := s.ServiceSummary

		// Находим план по умолчанию
		var targetPlan *ServicePlan
		for i := range s.Plans {
			if strings.EqualFold(s.Plans[i].ID, s.DefaultPlanName) || strings.EqualFold(s.Plans[i].Name, s.DefaultPlanName) {
				targetPlan = &s.Plans[i]
				break
			}
		}
		if targetPlan == nil && len(s.Plans) > 0 {
			targetPlan = &s.Plans[0]
		}

		if targetPlan != nil && len(targetPlan.Prices) > 0 {
			// Находим цену в США как базовую
			var usPriceUSD float64 = 0
			for _, p := range targetPlan.Prices {
				if p.CountryCode == "US" {
					ratesMutex.RLock()
					rate := SupportedCurrencies[p.Currency]
					ratesMutex.RUnlock()
					usPriceUSD = p.OriginalPrice * rate
					break
				}
			}
			if usPriceUSD == 0 {
				ratesMutex.RLock()
				rate := SupportedCurrencies[targetPlan.Prices[0].Currency]
				ratesMutex.RUnlock()
				usPriceUSD = targetPlan.Prices[0].OriginalPrice * rate
			}

			// Находим самую дешевую доступную страну
			cheapestUSD := math.MaxFloat64
			var cheapestPrice PlanPrice
			hasAvailable := false

			for _, p := range targetPlan.Prices {
				if p.Status == "not_available" || p.Status == "suspended" {
					continue
				}
				ratesMutex.RLock()
				rate := SupportedCurrencies[p.Currency]
				ratesMutex.RUnlock()
				pUSD := p.OriginalPrice * rate
				if pUSD < cheapestUSD && pUSD > 0 {
					cheapestUSD = pUSD
					cheapestPrice = p
					hasAvailable = true
				}
			}

			if hasAvailable {
				summary.CheapestCountry = cheapestPrice.CountryName
				summary.CheapestFlag = cheapestPrice.Flag
				summary.CheapestPriceUSD = math.Round(cheapestUSD*100) / 100
				summary.CheapestPrice = convertCurrency(cheapestUSD, "USD", targetCurrency)
				summary.CheapestCurrency = targetCurrency

				summary.USPriceUSD = math.Round(usPriceUSD*100) / 100
				summary.USPrice = convertCurrency(usPriceUSD, "USD", targetCurrency)

				if usPriceUSD > 0 {
					discount := (1.0 - (cheapestUSD / usPriceUSD)) * 100.0
					if discount < 0 {
						discount = 0
					}
					summary.MaxDiscount = math.Round(discount*10) / 10
				}
			}
			summary.CountriesCount = len(targetPlan.Prices)
		}

		summaries = append(summaries, summary)
	}

	return summaries
}

func handleServices(w http.ResponseWriter, r *http.Request) {
	targetCur := strings.ToUpper(r.URL.Query().Get("currency"))
	ratesMutex.RLock()
	validRate := SupportedCurrencies[targetCur] > 0
	ratesMutex.RUnlock()
	if targetCur == "" || !validRate {
		targetCur = "USD"
	}

	search := strings.ToLower(strings.TrimSpace(r.URL.Query().Get("search")))
	category := strings.TrimSpace(r.URL.Query().Get("category"))
	sortBy := r.URL.Query().Get("sort") // discount, price_asc, price_desc, name, popularity

	list := computeServiceSummaries(targetCur)

	// Filter
	var filtered []ServiceSummary
	for _, item := range list {
		if search != "" {
			nameMatch := strings.Contains(strings.ToLower(item.Name), search)
			catMatch := strings.Contains(strings.ToLower(item.Category), search)
			descMatch := strings.Contains(strings.ToLower(item.Description), search)
			if !nameMatch && !catMatch && !descMatch {
				continue
			}
		}
		if category != "" && category != "all" && !strings.EqualFold(item.Category, category) {
			continue
		}
		filtered = append(filtered, item)
	}

	// Sort
	switch sortBy {
	case "discount":
		sort.Slice(filtered, func(i, j int) bool {
			return filtered[i].MaxDiscount > filtered[j].MaxDiscount
		})
	case "price_asc":
		sort.Slice(filtered, func(i, j int) bool {
			return filtered[i].CheapestPrice < filtered[j].CheapestPrice
		})
	case "price_desc":
		sort.Slice(filtered, func(i, j int) bool {
			return filtered[i].CheapestPrice > filtered[j].CheapestPrice
		})
	case "name":
		sort.Slice(filtered, func(i, j int) bool {
			return filtered[i].Name < filtered[j].Name
		})
	default: // popularity
		sort.Slice(filtered, func(i, j int) bool {
			return filtered[i].PopularityRank < filtered[j].PopularityRank
		})
	}

	json.NewEncoder(w).Encode(filtered)
}

func handleServiceDetail(w http.ResponseWriter, r *http.Request) {
	pathParts := strings.Split(strings.Trim(r.URL.Path, "/"), "/")
	if len(pathParts) < 3 {
		http.Error(w, `{"error":"invalid service id"}`, http.StatusBadRequest)
		return
	}
	id := pathParts[2]

	targetCur := strings.ToUpper(r.URL.Query().Get("currency"))
	ratesMutex.RLock()
	validRate := SupportedCurrencies[targetCur] > 0
	ratesMutex.RUnlock()
	if targetCur == "" || !validRate {
		targetCur = "USD"
	}

	rawServicesMutex.RLock()
	var found *ServiceDetail
	for _, s := range RawServicesData {
		if strings.EqualFold(s.ID, id) || strings.EqualFold(s.Slug, id) {
			copyS := s
			found = &copyS
			break
		}
	}
	rawServicesMutex.RUnlock()

	if found == nil {
		http.Error(w, `{"error":"service not found"}`, http.StatusNotFound)
		return
	}

	for pIdx := range found.Plans {
		plan := &found.Plans[pIdx]

		var usPriceUSD float64 = 0
		for _, price := range plan.Prices {
			if price.CountryCode == "US" {
				ratesMutex.RLock()
				rate := SupportedCurrencies[price.Currency]
				ratesMutex.RUnlock()
				usPriceUSD = price.OriginalPrice * rate
				break
			}
		}
		if usPriceUSD == 0 && len(plan.Prices) > 0 {
			ratesMutex.RLock()
			rate := SupportedCurrencies[plan.Prices[0].Currency]
			ratesMutex.RUnlock()
			usPriceUSD = plan.Prices[0].OriginalPrice * rate
		}

		for cIdx := range plan.Prices {
			price := &plan.Prices[cIdx]

			if price.Status == "" {
				price.Status = "available"
			}
			switch price.Status {
			case "not_available":
				price.StatusLabel = "Не запущен"
			case "global_usd":
				price.StatusLabel = "Global $"
			case "suspended":
				price.StatusLabel = "Приостановлен"
			default:
				price.StatusLabel = "Доступен"
			}

			ratesMutex.RLock()
			rate := SupportedCurrencies[price.Currency]
			ratesMutex.RUnlock()

			usd := price.OriginalPrice * rate
			price.ConvertedPriceUSD = math.Round(usd*100) / 100
			price.TargetPrice = convertCurrency(usd, "USD", targetCur)
			price.TargetCurrency = targetCur

			if usPriceUSD > 0 && price.Status == "available" {
				disc := (1.0 - (usd / usPriceUSD)) * 100.0
				price.DiscountPercent = math.Round(disc*10) / 10
			}
		}

		sort.Slice(plan.Prices, func(i, j int) bool {
			// Доступные сначала, недоступные в конце
			if plan.Prices[i].Status != plan.Prices[j].Status {
				if plan.Prices[i].Status == "available" {
					return true
				}
				if plan.Prices[j].Status == "available" {
					return false
				}
			}
			return plan.Prices[i].ConvertedPriceUSD < plan.Prices[j].ConvertedPriceUSD
		})
	}

	summaries := computeServiceSummaries(targetCur)
	for _, sum := range summaries {
		if sum.ID == found.ID {
			found.ServiceSummary = sum
			break
		}
	}

	json.NewEncoder(w).Encode(found)
}

type MatrixRow struct {
	ServiceID   string             `json:"service_id"`
	ServiceName string             `json:"service_name"`
	Category    string             `json:"category"`
	Icon        string             `json:"icon"`
	Prices      map[string]float64 `json:"prices"`
	Statuses    map[string]string  `json:"statuses"` // CountryCode -> "available", "not_available", "global_usd"
	BestCountry string             `json:"best_country"`
	MaxDiscount float64            `json:"max_discount"`
}

func handleMatrix(w http.ResponseWriter, r *http.Request) {
	targetCur := strings.ToUpper(r.URL.Query().Get("currency"))
	ratesMutex.RLock()
	validRate := SupportedCurrencies[targetCur] > 0
	ratesMutex.RUnlock()
	if targetCur == "" || !validRate {
		targetCur = "USD"
	}

	rawServicesMutex.RLock()
	defer rawServicesMutex.RUnlock()

	var rows []MatrixRow
	for _, s := range RawServicesData {
		row := MatrixRow{
			ServiceID:   s.ID,
			ServiceName: s.Name,
			Category:    s.Category,
			Icon:        s.Icon,
			Prices:      make(map[string]float64),
			Statuses:    make(map[string]string),
		}

		if len(s.Plans) > 0 {
			plan := s.Plans[0]
			var usPriceUSD float64
			for _, p := range plan.Prices {
				if p.CountryCode == "US" {
					ratesMutex.RLock()
					rate := SupportedCurrencies[p.Currency]
					ratesMutex.RUnlock()
					usPriceUSD = p.OriginalPrice * rate
					break
				}
			}

			cheapestUSD := math.MaxFloat64
			bestCountry := ""

			for _, p := range plan.Prices {
				ratesMutex.RLock()
				rate := SupportedCurrencies[p.Currency]
				ratesMutex.RUnlock()

				usd := p.OriginalPrice * rate
				row.Prices[p.CountryCode] = convertCurrency(usd, "USD", targetCur)

				status := p.Status
				if status == "" {
					status = "available"
				}
				row.Statuses[p.CountryCode] = status

				if status == "available" && usd < cheapestUSD && usd > 0 {
					cheapestUSD = usd
					bestCountry = p.CountryCode
				}
			}

			row.BestCountry = bestCountry
			if usPriceUSD > 0 && cheapestUSD < math.MaxFloat64 {
				row.MaxDiscount = math.Round((1.0-(cheapestUSD/usPriceUSD))*1000) / 10
			}
		}

		rows = append(rows, row)
	}

	json.NewEncoder(w).Encode(rows)
}

func handleSuggest(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	var req SuggestionRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, `{"error":"invalid json body"}`, http.StatusBadRequest)
		return
	}

	suggestionsLock.Lock()
	savedSuggestions = append(savedSuggestions, req)
	suggestionsLock.Unlock()

	json.NewEncoder(w).Encode(map[string]interface{}{
		"success": true,
		"message": "Спасибо! Ваше предложение цены принято на проверку.",
		"count":   len(savedSuggestions),
	})
}

func handleManualSync(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	go func() {
		ctx, cancel := context.WithTimeout(context.Background(), 2*time.Minute)
		defer cancel()
		scheduler.RunSync(ctx)
	}()

	json.NewEncoder(w).Encode(map[string]interface{}{
		"success": true,
		"message": "Фоновая синхронизация запущена.",
	})
}

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	// Инициализируем планировщик провайдеров
	scheduler = NewSyncScheduler()

	// Запускаем немедленную синхронизацию в фоне при старте
	go func() {
		ctx, cancel := context.WithTimeout(context.Background(), 2*time.Minute)
		defer cancel()
		scheduler.RunSync(ctx)
	}()

	// Периодический планировщик раз в 24 часа
	go func() {
		ticker := time.NewTicker(24 * time.Hour)
		defer ticker.Stop()
		for range ticker.C {
			ctx, cancel := context.WithTimeout(context.Background(), 5*time.Minute)
			scheduler.RunSync(ctx)
			cancel()
		}
	}()

	mux := http.NewServeMux()

	// API Routes
	mux.HandleFunc("/api/health", corsMiddleware(handleHealth))
	mux.HandleFunc("/api/currencies", corsMiddleware(handleCurrencies))
	mux.HandleFunc("/api/countries", corsMiddleware(handleCountries))
	mux.HandleFunc("/api/services", corsMiddleware(handleServices))
	mux.HandleFunc("/api/services/", corsMiddleware(handleServiceDetail))
	mux.HandleFunc("/api/matrix", corsMiddleware(handleMatrix))
	mux.HandleFunc("/api/suggest", corsMiddleware(handleSuggest))
	mux.HandleFunc("/api/sync", corsMiddleware(handleManualSync))

	// Static files (dist if built)
	fs := http.FileServer(http.Dir("../dist"))
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if strings.HasPrefix(r.URL.Path, "/api/") {
			http.NotFound(w, r)
			return
		}
		path := "../dist" + r.URL.Path
		if _, err := os.Stat(path); os.IsNotExist(err) {
			http.ServeFile(w, r, "../dist/index.html")
			return
		}
		fs.ServeHTTP(w, r)
	})

	server := &http.Server{
		Addr:    ":" + port,
		Handler: mux,
	}

	fmt.Printf("🚀 SubDB Go Backend v2.0 running on http://localhost:%s\n", port)
	log.Fatal(server.ListenAndServe())
}
