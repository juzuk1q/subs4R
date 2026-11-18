# scripts/data_ai.py
# AI and Developer Intelligence services

AI_SERVICES = [
    {
        "id": "chatgpt-plus",
        "name": "ChatGPT Plus",
        "slug": "chatgpt-plus",
        "category": "AI & Software",
        "icon": "Bot",
        "color": "#10A37F",
        "description": "Доступ к GPT-4o, o1, Canvas, генерации DALL-E и передовым инструментам анализа.",
        "default_plan_name": "Plus Monthly",
        "popularity_rank": 5,
        "available_plans": ["Plus Monthly"],
        "official_url": "https://chatgpt.com",
        "guide": "Веб-версия стоит $20 глобально. Через мобильное приложение (турецкий Apple ID / нигерийский Google Play) можно оплачивать подарочными картами.",
        "is_global_usd": True,
        "plans": [
            {
                "id": "plus-monthly", "name": "Plus Monthly", "period": "month", "desc": "Полный доступ к GPT-4o, o1, Canvas.", "us_price": 20.0,
                "prices": {
                    "US": {"amount": 20.00, "curr": "USD", "source": "official", "avail": True, "notes": "Базовая цена OpenAI", "diff": "easy"},
                    "EU": {"amount": 22.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Включает НДС 20-23%", "diff": "easy"},
                    "GB": {"amount": 19.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Включает британский VAT 20%", "diff": "easy"},
                    "TR": {"amount": 649.99, "curr": "TRY", "source": "store", "avail": True, "notes": "Через турецкий iOS App Store", "diff": "easy"},
                    "NG": {"amount": 19900, "curr": "NGN", "source": "store", "avail": True, "notes": "Через Google Play Нигерии", "diff": "medium"},
                    "UA": {"amount": 20.00, "curr": "USD", "source": "usd_flat", "avail": True, "notes": "Оплата картами Украины (Monobank, Приват)", "diff": "easy"},
                    "KZ": {"amount": 20.00, "curr": "USD", "source": "usd_flat", "avail": True, "notes": "Карты Kaspi / Halyk", "diff": "easy"},
                    "PL": {"amount": 22.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Европейский биллинг с НДС", "diff": "easy"},
                    "IN": {"amount": 1999, "curr": "INR", "source": "store", "avail": True, "notes": "Через индийский App Store / Google Play", "diff": "medium"},
                    "AR": {"amount": 20.00, "curr": "USD", "source": "usd_flat", "avail": True, "notes": "Биллинг в USD", "diff": "hard"},
                    "BR": {"amount": 20.00, "curr": "USD", "source": "usd_flat", "avail": True, "notes": "Биллинг в USD", "diff": "medium"},
                    "EG": {"amount": 20.00, "curr": "USD", "source": "usd_flat", "avail": True, "notes": "Биллинг в USD", "diff": "medium"},
                    "PH": {"amount": 20.00, "curr": "USD", "source": "usd_flat", "avail": True, "notes": "Биллинг в USD", "diff": "easy"},
                    "JP": {"amount": 3000, "curr": "JPY", "source": "store", "avail": True, "notes": "Через японский App Store", "diff": "medium"},
                    "RU": {"amount": 20.00, "curr": "USD", "source": "usd_flat", "avail": False, "status": "suspended", "label": "Геоблок в РФ", "notes": "OpenAI блокирует доступ с IP РФ и карты российских банков.", "diff": "impossible"}
                }
            }
        ]
    },
    {
        "id": "claude-pro",
        "name": "Claude Pro",
        "slug": "claude-pro",
        "category": "AI & Software",
        "icon": "Sparkles",
        "color": "#D97706",
        "description": "Доступ к Claude 3.5 Sonnet, расширенный контекст, проекты и артефакты от Anthropic.",
        "default_plan_name": "Pro Monthly",
        "popularity_rank": 6,
        "available_plans": ["Pro Monthly"],
        "official_url": "https://claude.ai",
        "guide": "Anthropic биллит в долларах США ($20 + местный налог). В Европе добавляется VAT 20%. Российские карты и IP заблокированы.",
        "is_global_usd": True,
        "plans": [
            {
                "id": "pro-monthly", "name": "Pro Monthly", "period": "month", "desc": "5x лимиты, Claude 3.5 Sonnet & Opus, Projects.", "us_price": 20.0,
                "prices": {
                    "US": {"amount": 20.00, "curr": "USD", "source": "official", "avail": True, "notes": "Базовая цена Anthropic", "diff": "easy"},
                    "EU": {"amount": 22.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Включает VAT", "diff": "easy"},
                    "GB": {"amount": 20.00, "curr": "GBP", "source": "official", "avail": True, "notes": "Включает британский VAT 20%", "diff": "easy"},
                    "RU": {"amount": 20.00, "curr": "USD", "source": "usd_flat", "avail": False, "status": "suspended", "label": "Геоблок в РФ", "notes": "Anthropic блокирует аккаунты и платежи из РФ.", "diff": "impossible"}
                }
            }
        ]
    },
    {
        "id": "gemini-advanced",
        "name": "Google Gemini Advanced",
        "slug": "gemini-advanced",
        "category": "AI & Software",
        "icon": "Cpu",
        "color": "#1A73E8",
        "description": "Gemini 1.5 Pro с контекстом 1-2M токенов, интеграция с Gmail/Docs и 2ТБ Google One.",
        "default_plan_name": "AI Premium 2TB",
        "popularity_rank": 7,
        "available_plans": ["AI Premium 2TB"],
        "official_url": "https://gemini.google.com/advanced",
        "guide": "Подписка идет в составе тарифа Google One AI Premium 2TB. Оплачивается через Google Pay или баланс Google Play.",
        "plans": [
            {
                "id": "ai-premium-2tb", "name": "AI Premium 2TB", "period": "month", "desc": "Gemini Advanced + 2 ТБ в Google Диске.", "us_price": 19.99,
                "prices": {
                    "TR": {"amount": 719.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Турецкий Google One", "diff": "medium"},
                    "IN": {"amount": 1950, "curr": "INR", "source": "official", "avail": True, "notes": "Индийский Google One", "diff": "easy"},
                    "NG": {"amount": 19500, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерия Google Play", "diff": "medium"},
                    "UA": {"amount": 499, "curr": "UAH", "source": "official", "avail": True, "notes": "Прямая оплата картой", "diff": "easy"},
                    "KZ": {"amount": 8500, "curr": "KZT", "source": "official", "avail": True, "notes": "Карты Kaspi/Halyk", "diff": "easy"},
                    "AR": {"amount": 19999, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентинский Google One", "diff": "hard"},
                    "BR": {"amount": 96.99, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "PL": {"amount": 97.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "EU": {"amount": 21.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "US": {"amount": 19.99, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "GB": {"amount": 18.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "JP": {"amount": 2900, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EG": {"amount": 499, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 1099, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "RU": {"amount": 19.99, "curr": "USD", "source": "usd_flat", "avail": False, "status": "suspended", "label": "Google Play отключен", "notes": "Google отключил платежную систему Google Play в РФ.", "diff": "impossible"}
                }
            }
        ]
    },
    {
        "id": "perplexity-pro",
        "name": "Perplexity Pro",
        "slug": "perplexity-pro",
        "category": "AI & Software",
        "icon": "Search",
        "color": "#20B2AA",
        "description": "Безлимитный Copilot, выбор топовых моделей (GPT-4o, Claude 3.5 Sonnet, Sonar) и анализ файлов.",
        "default_plan_name": "Pro Monthly",
        "popularity_rank": 8,
        "available_plans": ["Pro Monthly"],
        "official_url": "https://www.perplexity.ai/pro",
        "guide": "Глобальный прайс $20/мес. Оплата через Stripe зарубежными картами.",
        "is_global_usd": True,
        "plans": [
            {
                "id": "pro-monthly", "name": "Pro Monthly", "period": "month", "desc": "Безлимитный Pro Search, Claude 3.5, GPT-4o.", "us_price": 20.0,
                "prices": {
                    "US": {"amount": 20.00, "curr": "USD", "source": "official", "avail": True, "notes": "Базовая цена", "diff": "easy"},
                    "EU": {"amount": 22.99, "curr": "EUR", "source": "official", "avail": True, "notes": "С учетом НДС", "diff": "easy"},
                    "RU": {"amount": 20.00, "curr": "USD", "source": "usd_flat", "avail": False, "status": "suspended", "label": "Блокировка карт РФ", "notes": "Stripe не принимает карты российских банков.", "diff": "impossible"}
                }
            }
        ]
    },
    {
        "id": "cursor-pro",
        "name": "Cursor Pro",
        "slug": "cursor-pro",
        "category": "AI & Software",
        "icon": "Code",
        "color": "#7C3AED",
        "description": "Главный AI-редактор кода: умный автокомплит, Composer, мульти-файловые правки на базе Claude 3.5 Sonnet.",
        "default_plan_name": "Pro Monthly",
        "popularity_rank": 9,
        "available_plans": ["Pro Monthly"],
        "official_url": "https://www.cursor.com",
        "guide": "Прайс фиксирован в долларах США ($20/мес). Оплата только международными картами Visa/Mastercard.",
        "is_global_usd": True,
        "plans": [
            {
                "id": "pro-monthly", "name": "Pro Monthly", "period": "month", "desc": "500 быстрых запросов в месяц к Claude 3.5 Sonnet и GPT-4o.", "us_price": 20.0,
                "prices": {
                    "US": {"amount": 20.00, "curr": "USD", "source": "official", "avail": True, "notes": "Базовая цена", "diff": "easy"},
                    "RU": {"amount": 20.00, "curr": "USD", "source": "usd_flat", "avail": False, "status": "suspended", "label": "Оплата не проходит", "notes": "Stripe блокирует платежи картами РФ.", "diff": "impossible"}
                }
            }
        ]
    },
    {
        "id": "grok-x-premium",
        "name": "X Premium & Grok",
        "slug": "grok-x-premium",
        "category": "Social & AI",
        "icon": "Zap",
        "color": "#000000",
        "description": "Доступ к Grok 2, синяя галочка, монетизация и отсутствие рекламы в ленте X (Twitter).",
        "default_plan_name": "Premium Monthly",
        "popularity_rank": 10,
        "available_plans": ["Premium Monthly"],
        "official_url": "https://x.com",
        "guide": "В Турции и Нигерии стоимость подписки через веб или мобильные сторы в несколько раз ниже цены США.",
        "plans": [
            {
                "id": "premium-monthly", "name": "Premium Monthly", "period": "month", "desc": "Grok AI, синяя галочка, редактор постов.", "us_price": 8.0,
                "prices": {
                    "TR": {"amount": 156.00, "curr": "TRY", "source": "official", "avail": True, "notes": "Турецкий биллинг в веб", "diff": "medium"},
                    "NG": {"amount": 3500, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерия", "diff": "medium"},
                    "IN": {"amount": 650, "curr": "INR", "source": "official", "avail": True, "notes": "Индия", "diff": "easy"},
                    "AR": {"amount": 4500, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентина", "diff": "hard"},
                    "BR": {"amount": 42.00, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "UA": {"amount": 8.00, "curr": "USD", "source": "official", "avail": True, "notes": "Биллинг в USD", "diff": "easy"},
                    "KZ": {"amount": 8.00, "curr": "USD", "source": "official", "avail": True, "notes": "Казахстан", "diff": "easy"},
                    "PL": {"amount": 36.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "EU": {"amount": 8.00, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 9.60, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 8.00, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "JP": {"amount": 980, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EG": {"amount": 179.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 399, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "RU": {"amount": 8.00, "curr": "USD", "source": "usd_flat", "avail": False, "status": "suspended", "label": "X заблокирован в РФ", "notes": "Соцсеть X заблокирована на территории РФ.", "diff": "impossible"}
                }
            }
        ]
    },
    {
        "id": "midjourney",
        "name": "Midjourney",
        "slug": "midjourney",
        "category": "AI & Creativity",
        "icon": "Image",
        "color": "#000000",
        "description": "Лучшая модель генерации арта, фотореализма и концептов прямо через Discord или Web.",
        "default_plan_name": "Standard Plan",
        "popularity_rank": 26,
        "available_plans": ["Standard Plan"],
        "official_url": "https://www.midjourney.com",
        "guide": "Midjourney продается только в долларах ($30/мес за Standard с безлимитным Relax-режимом).",
        "is_global_usd": True,
        "plans": [
            {
                "id": "standard", "name": "Standard Plan", "period": "month", "desc": "15 часов Fast GPU + безлимитный Relax GPU.", "us_price": 30.0,
                "prices": {
                    "US": {"amount": 30.00, "curr": "USD", "source": "official", "avail": True, "notes": "Базовая цена", "diff": "easy"},
                    "EU": {"amount": 34.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Включает НДС ЕС", "diff": "easy"},
                    "RU": {"amount": 30.00, "curr": "USD", "source": "usd_flat", "avail": False, "status": "suspended", "label": "Блокировка карт РФ", "notes": "Stripe блокирует оплату российскими картами.", "diff": "impossible"}
                }
            }
        ]
    },
    {
        "id": "elevenlabs",
        "name": "ElevenLabs",
        "slug": "elevenlabs",
        "category": "AI & Voice",
        "icon": "Volume2",
        "color": "#000000",
        "description": "Самый реалистичный ИИ-генератор голоса, клонирование речи и озвучка на 32 языках.",
        "default_plan_name": "Starter Monthly",
        "popularity_rank": 27,
        "available_plans": ["Starter Monthly"],
        "official_url": "https://elevenlabs.io",
        "guide": "Глобальный прайс в долларах США ($5/мес за тариф Starter). Оплата зарубежными картами.",
        "is_global_usd": True,
        "plans": [
            {
                "id": "starter-monthly", "name": "Starter Monthly", "period": "month", "desc": "30,000 символов в месяц, клонирование до 3 голосов.", "us_price": 5.0,
                "prices": {
                    "US": {"amount": 5.00, "curr": "USD", "source": "official", "avail": True, "notes": "Базовая цена", "diff": "easy"},
                    "RU": {"amount": 5.00, "curr": "USD", "source": "usd_flat", "avail": False, "status": "suspended", "label": "Оплата картами РФ закрыта", "notes": "Stripe не принимает карты банков РФ.", "diff": "impossible"}
                }
            }
        ]
    },
    {
        "id": "deepl-pro",
        "name": "DeepL Pro",
        "slug": "deepl-pro",
        "category": "AI & Translation",
        "icon": "Languages",
        "color": "#0F2B46",
        "description": "Нейросетевой перевод текстов и документов без ограничений с защитой данных.",
        "default_plan_name": "Starter Monthly",
        "popularity_rank": 28,
        "available_plans": ["Starter Monthly"],
        "official_url": "https://www.deepl.com/pro",
        "guide": "Официальные продажи ведутся в EUR / USD. Для пользователей из РФ покупка заблокирована.",
        "is_global_usd": True,
        "plans": [
            {
                "id": "starter", "name": "Starter Monthly", "period": "month", "desc": "Безлимитный перевод текста, 5 документов в месяц.", "us_price": 8.74,
                "prices": {
                    "US": {"amount": 8.74, "curr": "USD", "source": "official", "avail": True, "notes": "Базовая цена США", "diff": "easy"},
                    "EU": {"amount": 7.49, "curr": "EUR", "source": "official", "avail": True, "notes": "Базовая цена в Еврозоне", "diff": "easy"},
                    "PL": {"amount": 34.00, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "GB": {"amount": 7.49, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "RU": {"amount": 8.74, "curr": "USD", "source": "usd_flat", "avail": False, "status": "suspended", "label": "DeepL Pro заблокирован в РФ", "notes": "DeepL прекратил продажу Pro подписок в РФ.", "diff": "impossible"}
                }
            }
        ]
    }
]

print("AI Services definitions loaded")
