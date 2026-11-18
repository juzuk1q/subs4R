package parser

import (
	"context"
	"time"
)

type SourceType string

const (
	SourceOfficial  SourceType = "official"  // 1. Официальная страница цен сервиса
	SourceStore     SourceType = "store"     // 2. Региональный App Store / Google Play / Steam
	SourceUSDFlat   SourceType = "usd_flat"  // 3. Единая цена в USD с учетом местного налога
	SourceCommunity SourceType = "community" // 4. Агрегаторы, Wikipedia, GitHub, /api/suggest
	SourceArchive   SourceType = "archive"   // 5. Wayback Machine (archive.org)
	SourceEstimated SourceType = "estimated" // 6. Оценка по PPP / соседним странам
)

// PriceResult представляет результат работы цепочки резолвера
type PriceResult struct {
	Amount        float64    `json:"amount"`
	Currency      string     `json:"currency"`
	Period        string     `json:"period"` // month, year
	IncludesTax   bool       `json:"includes_tax"`
	Source        SourceType `json:"source"`
	SourceURL     string     `json:"source_url"`
	SourceDate    string     `json:"source_date"` // YYYY-MM-DD
	FetchedAt     time.Time  `json:"fetched_at"`
	Available     bool       `json:"available"`    // доступен ли сервис официально в стране
	Status        string     `json:"status"`       // "available", "not_available", "global_usd", "suspended"
	StatusLabel   string     `json:"status_label"` // Человекочитаемый статус
	PaymentDifficulty string `json:"payment_difficulty"`
	PaymentNotes  string     `json:"payment_notes"`
	NeedsReview   bool       `json:"needs_review"` // выброс > 5x от цены США
}

// ServiceAdapter интерфейс адаптера для конкретного сервиса
type ServiceAdapter interface {
	ID() string
	Name() string
	IsGlobalUSD() bool
	FetchOfficial(ctx context.Context, plan string, country string) (*PriceResult, error)
	FetchStore(ctx context.Context, plan string, country string) (*PriceResult, error)
}
