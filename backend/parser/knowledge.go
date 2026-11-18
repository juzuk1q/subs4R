package parser

// initKnowledgeBases наполняет базы community и archive проверенными данными
func (r *Resolver) initKnowledgeBases() {
	// ==================== ARCHIVE DB (archive.org snapshots) ====================
	// Исторические официальные цены на момент ухода сервисов с рынка РФ (снэпшоты 2021-2022)
	r.archiveDB["spotify"] = map[string]PriceResult{
		"RU": {
			Amount: 169, Currency: "RUB", Period: "month", Source: SourceArchive,
			SourceURL: "https://web.archive.org/web/20220201000000/https://www.spotify.com/ru-ru/premium/",
			SourceDate: "2022-02-01", Available: false, Status: "suspended", StatusLabel: "Ушел из РФ",
			PaymentDifficulty: "impossible", PaymentNotes: "Сервис прекратил работу в РФ в апреле 2022. Архивный тариф: 169 ₽/мес.",
		},
	}

	r.archiveDB["netflix"] = map[string]PriceResult{
		"RU": {
			Amount: 599, Currency: "RUB", Period: "month", Source: SourceArchive,
			SourceURL: "https://web.archive.org/web/20220215000000/https://www.netflix.com/ru/",
			SourceDate: "2022-02-15", Available: false, Status: "suspended", StatusLabel: "Ушел из РФ",
			PaymentDifficulty: "impossible", PaymentNotes: "Netflix остановил работу в РФ в марте 2022. Архивный базовый план: 599 ₽/мес.",
		},
	}

	r.archiveDB["deezer"] = map[string]PriceResult{
		"RU": {
			Amount: 169, Currency: "RUB", Period: "month", Source: SourceArchive,
			SourceURL: "https://web.archive.org/web/20220110000000/https://www.deezer.com/ru/offers",
			SourceDate: "2022-01-10", Available: false, Status: "suspended", StatusLabel: "Ушел из РФ",
			PaymentDifficulty: "impossible", PaymentNotes: "Deezer покинул рынок РФ. Архивный тариф: 169 ₽/мес.",
		},
	}

	r.archiveDB["youtube-premium"] = map[string]PriceResult{
		"RU": {
			Amount: 199, Currency: "RUB", Period: "month", Source: SourceArchive,
			SourceURL: "https://web.archive.org/web/20220220000000/https://www.youtube.com/premium",
			SourceDate: "2022-02-20", Available: false, Status: "suspended", StatusLabel: "Отключен в РФ",
			PaymentDifficulty: "impossible", PaymentNotes: "YouTube приостановил монетизацию и платные подписки в РФ в марте 2022. Архивный тариф: 199 ₽/мес.",
		},
	}

	r.archiveDB["playstation-plus"] = map[string]PriceResult{
		"RU": {
			Amount: 529, Currency: "RUB", Period: "month", Source: SourceArchive,
			SourceURL: "https://web.archive.org/web/20220201000000/https://store.playstation.com/ru-ru/",
			SourceDate: "2022-02-01", Available: false, Status: "suspended", StatusLabel: "PS Store заморожен",
			PaymentDifficulty: "impossible", PaymentNotes: "Sony заморозила PlayStation Store в РФ в марте 2022. Архивный тариф: 529 ₽/мес.",
		},
	}

	r.archiveDB["nintendo-switch-online"] = map[string]PriceResult{
		"RU": {
			Amount: 1399, Currency: "RUB", Period: "year", Source: SourceArchive,
			SourceURL: "https://web.archive.org/web/20220210000000/https://www.nintendo.ru/switch/online",
			SourceDate: "2022-02-10", Available: false, Status: "suspended", StatusLabel: "eShop закрыт",
			PaymentDifficulty: "impossible", PaymentNotes: "Nintendo eShop в РФ закрыт на бессрочное обслуживание. Архивный годовой тариф: 1399 ₽.",
		},
	}

	r.archiveDB["tidal"] = map[string]PriceResult{
		"TR": {
			Amount: 39.99, Currency: "TRY", Period: "month", Source: SourceArchive,
			SourceURL: "https://web.archive.org/web/20220801000000/https://tidal.com/pricing",
			SourceDate: "2022-08-01", Available: false, Status: "suspended", StatusLabel: "Ушел из Турции",
			PaymentDifficulty: "impossible", PaymentNotes: "Tidal ушел из Турции из-за требований регулятора RTUK. Последняя цена: 39.99 TRY.",
		},
		"RU": {
			Amount: 9.99, Currency: "USD", Period: "month", Source: SourceArchive,
			SourceURL: "https://web.archive.org/web/20220101000000/https://tidal.com/",
			SourceDate: "2022-01-01", Available: false, Status: "suspended", StatusLabel: "Недоступен в РФ",
			PaymentDifficulty: "impossible", PaymentNotes: "Официально никогда не запускался в РФ.",
		},
	}

	r.archiveDB["notion-plus"] = map[string]PriceResult{
		"RU": {
			Amount: 10, Currency: "USD", Period: "month", Source: SourceArchive,
			SourceURL: "https://web.archive.org/web/20240801000000/https://www.notion.so/pricing",
			SourceDate: "2024-08-01", Available: false, Status: "suspended", StatusLabel: "Ушел из РФ",
			PaymentDifficulty: "impossible", PaymentNotes: "Notion заблокировал рабочие пространства из РФ в сентябре 2024.",
		},
	}

	r.archiveDB["tinder-gold"] = map[string]PriceResult{
		"RU": {
			Amount: 499, Currency: "RUB", Period: "month", Source: SourceArchive,
			SourceURL: "https://web.archive.org/web/20230501000000/https://tinder.com/",
			SourceDate: "2023-05-01", Available: false, Status: "suspended", StatusLabel: "Ушел из РФ",
			PaymentDifficulty: "impossible", PaymentNotes: "Match Group (Tinder) окончательно отключил сервера в РФ в июне 2023.",
		},
	}

	// ==================== COMMUNITY DB ====================
	// Данные краудсорсинга, агрегаторов и профильных сообществ
	r.communityDB["duolingo-super"] = map[string]PriceResult{
		"TR": {
			Amount: 49.99, Currency: "TRY", Period: "month", Source: SourceCommunity,
			SourceURL: "https://reddit.com/r/Duolingo/comments/pricing_turkey",
			SourceDate: "2026-01-15", Available: true, Status: "available", StatusLabel: "Доступен",
			PaymentDifficulty: "medium", PaymentNotes: "Оплата через турецкий App Store / Google Play",
		},
		"UA": {
			Amount: 4.99, Currency: "USD", Period: "month", Source: SourceCommunity,
			SourceURL: "https://community.duolingo.com",
			SourceDate: "2026-02-01", Available: true, Status: "available", StatusLabel: "Доступен",
			PaymentDifficulty: "easy", PaymentNotes: "Биллинг в USD картами украинских банков",
		},
		"KZ": {
			Amount: 5.49, Currency: "USD", Period: "month", Source: SourceCommunity,
			SourceURL: "https://community.duolingo.com",
			SourceDate: "2026-02-01", Available: true, Status: "available", StatusLabel: "Доступен",
			PaymentDifficulty: "easy", PaymentNotes: "Карты Kaspi / Halyk",
		},
		"AR": {
			Amount: 2499, Currency: "ARS", Period: "month", Source: SourceCommunity,
			SourceURL: "https://belo.app/blog/duolingo-precios-argentina",
			SourceDate: "2026-01-20", Available: true, Status: "available", StatusLabel: "Доступен",
			PaymentDifficulty: "hard", PaymentNotes: "Карты местных банков + цифровой налог",
		},
	}

	r.communityDB["canva-pro"] = map[string]PriceResult{
		"TR": {
			Amount: 84.99, Currency: "TRY", Period: "month", Source: SourceCommunity,
			SourceURL: "https://spoteeq.ru/canva", SourceDate: "2026-02-10",
			Available: true, Status: "available", StatusLabel: "Доступен",
			PaymentDifficulty: "medium", PaymentNotes: "Виртуальные карты Ininal / OlduBil",
		},
		"AR": {
			Amount: 3999, Currency: "ARS", Period: "month", Source: SourceCommunity,
			SourceURL: "https://spoteeq.ru/canva", SourceDate: "2026-02-10",
			Available: true, Status: "available", StatusLabel: "Доступен",
			PaymentDifficulty: "hard", PaymentNotes: "Аргентинские карты",
		},
		"IN": {
			Amount: 499, Currency: "INR", Period: "month", Source: SourceCommunity,
			SourceURL: "https://canva.com/en_in/pricing", SourceDate: "2026-01-10",
			Available: true, Status: "available", StatusLabel: "Доступен",
			PaymentDifficulty: "easy", PaymentNotes: "Индийские карты и UPI",
		},
	}
}
