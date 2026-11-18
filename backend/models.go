package main

import (
	"context"
	"errors"
	"time"
)

var (
	ErrNotAvailable = errors.New("not available in region")
	ErrGlobalUSD    = errors.New("charged in USD")
	ErrSuspended    = errors.New("service suspended in region")
)

type Country struct {
	Code     string `json:"code"`
	Name     string `json:"name"`
	Flag     string `json:"flag"`
	Currency string `json:"currency"`
	Symbol   string `json:"symbol"`
}

type PlanPrice struct {
	CountryCode       string    `json:"country_code"`
	CountryName       string    `json:"country_name"`
	Flag              string    `json:"flag"`
	Currency          string    `json:"currency"`
	Symbol            string    `json:"symbol"`
	OriginalPrice     float64   `json:"original_price"`
	ConvertedPriceUSD float64   `json:"converted_price_usd"`
	TargetPrice       float64   `json:"target_price"`
	TargetCurrency    string    `json:"target_currency"`
	DiscountPercent   float64   `json:"discount_percent"`   // относительно US
	PaymentDifficulty string    `json:"payment_difficulty"` // easy, medium, hard, impossible
	PaymentNotes      string    `json:"payment_notes"`
	PriceHistory      []float64 `json:"price_history"` // последние месяцы в USD
	Status            string    `json:"status"`        // "available", "not_available", "global_usd", "suspended"
	StatusLabel       string    `json:"status_label"`  // Человекочитаемый статус
	InclTax           bool      `json:"incl_tax"`
	Source            string    `json:"source"`         // "official", "store", "usd_flat", "community", "archive", "estimated"
	SourceURL         string    `json:"source_url"`     // URL источника цены
	SourceDate        string    `json:"source_date"`    // Дата источника (YYYY-MM-DD)
	FetchedAt         string    `json:"fetched_at"`
	NeedsReview       bool      `json:"needs_review"`
	Available         bool      `json:"available"`      // true даже для estimated, false только если вообще не запущен
}

type ServicePlan struct {
	ID          string      `json:"id"`
	Name        string      `json:"name"`
	Period      string      `json:"period"` // month, year
	Description string      `json:"description"`
	Prices      []PlanPrice `json:"prices"`
}

type ServiceSummary struct {
	ID               string   `json:"id"`
	Name             string   `json:"name"`
	Slug             string   `json:"slug"`
	Category         string   `json:"category"`
	Icon             string   `json:"icon"`
	Color            string   `json:"color"`
	Description      string   `json:"description"`
	DefaultPlanName  string   `json:"default_plan_name"`
	CheapestCountry  string   `json:"cheapest_country"`
	CheapestFlag     string   `json:"cheapest_flag"`
	CheapestPriceUSD float64  `json:"cheapest_price_usd"`
	CheapestPrice    float64  `json:"cheapest_price"`
	CheapestCurrency string   `json:"cheapest_currency"`
	USPriceUSD       float64  `json:"us_price_usd"`
	USPrice          float64  `json:"us_price"`
	MaxDiscount      float64  `json:"max_discount"`
	CountriesCount   int      `json:"countries_count"`
	AvailablePlans   []string `json:"available_plans"`
	PopularityRank   int      `json:"popularity_rank"`
}

type ServiceDetail struct {
	ServiceSummary
	OfficialURL string        `json:"official_url"`
	Guide       string        `json:"guide"`
	Plans       []ServicePlan `json:"plans"`
}

type SuggestionRequest struct {
	ServiceID     string  `json:"service_id"`
	CountryCode   string  `json:"country_code"`
	PlanName      string  `json:"plan_name"`
	ProposedPrice float64 `json:"proposed_price"`
	Currency      string  `json:"currency"`
	Notes         string  `json:"notes"`
	UserContact   string  `json:"user_contact"`
}

// Провайдерский слой
type Price struct {
	Amount      float64
	Currency    string // Валюта страны без пересчета ("TRY", "INR", "KZT")
	InclTax     bool
	Source      string
	FetchedAt   time.Time
	Status      string // "available", "not_available", "global_usd", "suspended"
	NeedsReview bool
}

type PlanRef struct {
	ServiceID  string
	PlanID     string
	MSBigID    string // BigId для Microsoft Store API
	SteamAppID int    // AppID для Steam Store API
	AppleAppID int64  // AppID для Apple App Store Lookup / SSR API
}

type Provider interface {
	Fetch(ctx context.Context, plan PlanRef, country string) (Price, error)
}
