package parser

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"
	"time"
)

// BaseAdapter базовая реализация интерфейса
type BaseAdapter struct {
	id          string
	name        string
	isGlobalUSD bool
}

func (b *BaseAdapter) ID() string         { return b.id }
func (b *BaseAdapter) Name() string       { return b.name }
func (b *BaseAdapter) IsGlobalUSD() bool  { return b.isGlobalUSD }

func (b *BaseAdapter) FetchOfficial(ctx context.Context, plan string, country string) (*PriceResult, error) {
	return nil, fmt.Errorf("no official web adapter for %s", b.id)
}

func (b *BaseAdapter) FetchStore(ctx context.Context, plan string, country string) (*PriceResult, error) {
	return nil, fmt.Errorf("no store adapter for %s", b.id)
}

// ==================== GLOBAL USD ADAPTER ====================
// Для SaaS, AI и Dev инструментов с единой мировой ценой в USD
type GlobalUSDAdapter struct {
	BaseAdapter
	basePriceUSD float64
}

func NewGlobalUSDAdapter(id, name string, basePriceUSD float64) *GlobalUSDAdapter {
	return &GlobalUSDAdapter{
		BaseAdapter: BaseAdapter{
			id:          id,
			name:        name,
			isGlobalUSD: true,
		},
		basePriceUSD: basePriceUSD,
	}
}

// ==================== MICROSOFT STORE ADAPTER ====================
type MSStoreAdapter struct {
	BaseAdapter
	bigIDs map[string]string // plan -> BigID
	client *http.Client
}

func NewMSStoreAdapter(id, name string, bigIDs map[string]string) *MSStoreAdapter {
	return &MSStoreAdapter{
		BaseAdapter: BaseAdapter{id: id, name: name, isGlobalUSD: false},
		bigIDs:      bigIDs,
		client:      &http.Client{Timeout: 8 * time.Second},
	}
}

func (a *MSStoreAdapter) FetchOfficial(ctx context.Context, plan string, country string) (*PriceResult, error) {
	bigID, ok := a.bigIDs[plan]
	if !ok || bigID == "" {
		return nil, fmt.Errorf("no bigID for plan %s", plan)
	}

	u := fmt.Sprintf(
		"https://displaycatalog.mp.microsoft.com/v7.0/products?bigIds=%s&market=%s&languages=en-US",
		bigID, strings.ToUpper(country),
	)

	req, err := http.NewRequestWithContext(ctx, "GET", u, nil)
	if err != nil {
		return nil, err
	}
	req.Header.Set("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) SubDB/1.0")

	resp, err := a.client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	if resp.StatusCode == 404 {
		return nil, fmt.Errorf("not available in market %s", country)
	}

	var r struct {
		Products []struct {
			DisplaySkuAvailabilities []struct {
				Availabilities []struct {
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
		return nil, err
	}

	if len(r.Products) == 0 {
		return nil, fmt.Errorf("product empty in market %s", country)
	}

	var bestPrice float64 = 0
	var curr string
	var taxIncluded bool

	for _, sku := range r.Products[0].DisplaySkuAvailabilities {
		for _, av := range sku.Availabilities {
			p := av.OrderManagementData.Price
			if p.ListPrice > 0 {
				if bestPrice == 0 || p.ListPrice < bestPrice {
					bestPrice = p.ListPrice
					curr = p.CurrencyCode
					taxIncluded = p.IsTaxIncluded
				}
			}
		}
	}

	if bestPrice == 0 {
		return nil, fmt.Errorf("zero price in MS Store for %s", country)
	}

	status := "available"
	if country != "US" && curr == "USD" {
		status = "global_usd"
	}

	return &PriceResult{
		Amount:            bestPrice,
		Currency:          curr,
		Period:            "month",
		IncludesTax:       taxIncluded,
		Source:            SourceOfficial,
		SourceURL:         u,
		SourceDate:        time.Now().Format("2006-01-02"),
		Available:         true,
		Status:            status,
		StatusLabel:       "Доступен",
		PaymentDifficulty: "medium",
		PaymentNotes:      "Официальный Microsoft Store. Принимает карты региона и Xbox Gift Cards.",
	}, nil
}

// ==================== STEAM STORE ADAPTER ====================
type SteamAdapter struct {
	BaseAdapter
	appIDs map[string]int
	client *http.Client
}

func NewSteamAdapter(id, name string, appIDs map[string]int) *SteamAdapter {
	return &SteamAdapter{
		BaseAdapter: BaseAdapter{id: id, name: name, isGlobalUSD: false},
		appIDs:      appIDs,
		client:      &http.Client{Timeout: 8 * time.Second},
	}
}

func (a *SteamAdapter) FetchStore(ctx context.Context, plan string, country string) (*PriceResult, error) {
	appID, ok := a.appIDs[plan]
	if !ok || appID == 0 {
		return nil, fmt.Errorf("no steam appID for plan %s", plan)
	}

	u := fmt.Sprintf(
		"https://store.steampowered.com/api/appdetails?appids=%d&cc=%s",
		appID, strings.ToLower(country),
	)

	req, err := http.NewRequestWithContext(ctx, "GET", u, nil)
	if err != nil {
		return nil, err
	}
	req.Header.Set("User-Agent", "Valve Steam Client")

	resp, err := a.client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	var res map[string]struct {
		Success bool `json:"success"`
		Data    struct {
			PriceOverview struct {
				Currency string  `json:"currency"`
				Final    float64 `json:"final"`
			} `json:"price_overview"`
		} `json:"data"`
	}

	if err := json.NewDecoder(resp.Body).Decode(&res); err != nil {
		return nil, err
	}

	appKey := fmt.Sprintf("%d", appID)
	item, ok := res[appKey]
	if !ok || !item.Success || item.Data.PriceOverview.Final == 0 {
		return nil, fmt.Errorf("steam price not available for %s", country)
	}

	amount := item.Data.PriceOverview.Final / 100.0
	curr := item.Data.PriceOverview.Currency

	status := "available"
	if country != "US" && curr == "USD" {
		status = "global_usd"
	}

	return &PriceResult{
		Amount:            amount,
		Currency:          curr,
		Period:            "month",
		IncludesTax:       true,
		Source:            SourceStore,
		SourceURL:         fmt.Sprintf("https://store.steampowered.com/app/%d", appID),
		SourceDate:        time.Now().Format("2006-01-02"),
		Available:         true,
		Status:            status,
		StatusLabel:       "Доступен",
		PaymentDifficulty: "easy",
		PaymentNotes:      "Официальный Steam Store. Оплата с баланса кошелька Steam или картами.",
	}, nil
}
