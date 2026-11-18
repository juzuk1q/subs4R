# scripts/data_video.py
# Video Streaming services

VIDEO_SERVICES = [
    {
        "id": "youtube-premium",
        "name": "YouTube Premium",
        "slug": "youtube-premium",
        "category": "Streaming Video",
        "icon": "Play",
        "color": "#FF0000",
        "description": "Видео без рекламы, фоновое воспроизведение, офлайн-загрузка и YouTube Music.",
        "default_plan_name": "Individual",
        "popularity_rank": 11,
        "available_plans": ["Individual", "Family"],
        "official_url": "https://www.youtube.com/premium",
        "guide": "Для подключения Турции или Нигерии требуется местный платежный метод (виртуальные карты Ininal, Geegpay). Для Украины подходят карты Monobank/ПриватБанк. В РФ монетизация и реклама отключены.",
        "plans": [
            {
                "id": "individual", "name": "Individual", "period": "month", "desc": "1 аккаунт, без рекламы, офлайн-загрузка, YouTube Music.", "us_price": 13.99,
                "prices": {
                    "NG": {"amount": 1700, "curr": "NGN", "source": "official", "avail": True, "notes": "Карты Geegpay / Chipper", "diff": "medium"},
                    "TR": {"amount": 79.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Карты Ininal, Papara", "diff": "medium"},
                    "IN": {"amount": 149, "curr": "INR", "source": "official", "avail": True, "notes": "Индийские карты с e-Mandate", "diff": "hard"},
                    "AR": {"amount": 2899, "curr": "ARS", "source": "official", "avail": True, "notes": "Карты банков Аргентины", "diff": "hard"},
                    "UA": {"amount": 99, "curr": "UAH", "source": "official", "avail": True, "notes": "Принимает карты украинских банков", "diff": "easy"},
                    "KZ": {"amount": 3500, "curr": "KZT", "source": "official", "avail": True, "notes": "Карты Kaspi, Halyk", "diff": "easy"},
                    "BR": {"amount": 24.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразильские карты", "diff": "medium"},
                    "PL": {"amount": 29.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Европейские карты и PayPal", "diff": "easy"},
                    "EG": {"amount": 89.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египетские карты", "diff": "medium"},
                    "PH": {"amount": 159, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "JP": {"amount": 1280, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EU": {"amount": 12.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 12.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 13.99, "curr": "USD", "source": "official", "avail": True, "notes": "Стандартная цена США", "diff": "easy"},
                    "RU": {"amount": 199, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Отключен в РФ", "notes": "YouTube приостановил платные подписки в РФ с марта 2022. Реклама отключена бесплатно. Архивный тариф: 199 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220220000000/https://www.youtube.com/premium", "date": "2022-02-20"}
                }
            },
            {
                "id": "family", "name": "Family", "period": "month", "desc": "До 5 членов семьи в одном доме.", "us_price": 22.99,
                "prices": {
                    "NG": {"amount": 3200, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерийские карты", "diff": "medium"},
                    "TR": {"amount": 159.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Турецкие карты Ininal/Papara", "diff": "medium"},
                    "IN": {"amount": 299, "curr": "INR", "source": "official", "avail": True, "notes": "Индийские карты", "diff": "hard"},
                    "AR": {"amount": 4999, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентина", "diff": "hard"},
                    "UA": {"amount": 149, "curr": "UAH", "source": "official", "avail": True, "notes": "Украинские карты", "diff": "easy"},
                    "KZ": {"amount": 5600, "curr": "KZT", "source": "official", "avail": True, "notes": "Карты Kaspi", "diff": "easy"},
                    "BR": {"amount": 41.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "PL": {"amount": 46.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "EG": {"amount": 149.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 239, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "JP": {"amount": 2280, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EU": {"amount": 23.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 19.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 22.99, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "RU": {"amount": 299, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Отключен в РФ", "notes": "Семейный тариф в РФ отключен. Архивный тариф: 299 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220220000000/https://www.youtube.com/premium", "date": "2022-02-20"}
                }
            }
        ]
    },
    {
        "id": "netflix",
        "name": "Netflix",
        "slug": "netflix",
        "category": "Streaming Video",
        "icon": "Tv",
        "color": "#E50914",
        "description": "Кино, сериалы и документальные фильмы в высоком качестве без рекламы.",
        "default_plan_name": "Standard",
        "popularity_rank": 12,
        "available_plans": ["Standard", "Premium"],
        "official_url": "https://www.netflix.com",
        "guide": "Netflix активирует геоблокировку на 28 дней при регистрации в Турции, Нигерии или Египте (просмотр первые 28 дней только с IP страны регистрации). После 28 дней блок снимается.",
        "plans": [
            {
                "id": "standard", "name": "Standard 1080p", "period": "month", "desc": "2 устройства одновременно, Full HD 1080p, без рекламы.", "us_price": 15.49,
                "prices": {
                    "NG": {"amount": 4000, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерийская карта, 28 дней геоблок", "diff": "medium"},
                    "EG": {"amount": 165, "curr": "EGP", "source": "official", "avail": True, "notes": "Египетская карта", "diff": "medium"},
                    "TR": {"amount": 229.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Подарочные карты Netflix Turkey (Gift Card)", "diff": "easy"},
                    "IN": {"amount": 499, "curr": "INR", "source": "official", "avail": True, "notes": "Индийские карты", "diff": "medium"},
                    "AR": {"amount": 5999, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентина (без учета налога 59%)", "diff": "hard"},
                    "BR": {"amount": 39.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразильские Gift Cards", "diff": "medium"},
                    "UA": {"amount": 7.49, "curr": "EUR", "source": "official", "avail": True, "notes": "Биллинг в EUR, без геоблоков", "diff": "easy"},
                    "KZ": {"amount": 7.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Карты Казахстана (EUR)", "diff": "easy"},
                    "PL": {"amount": 43.00, "curr": "PLN", "source": "official", "avail": True, "notes": "Польские и европейские карты", "diff": "easy"},
                    "PH": {"amount": 399, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "JP": {"amount": 1490, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EU": {"amount": 13.49, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 10.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 15.49, "curr": "USD", "source": "official", "avail": True, "notes": "Стандартная цена США", "diff": "easy"},
                    "RU": {"amount": 599, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Ушел из РФ", "notes": "Netflix ушел из РФ в марте 2022. Архивный базовый тариф: 599 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220215000000/https://www.netflix.com/ru/", "date": "2022-02-15"}
                }
            }
        ]
    },
    {
        "id": "crunchyroll",
        "name": "Crunchyroll Mega Fan",
        "slug": "crunchyroll",
        "category": "Streaming Video",
        "icon": "Film",
        "color": "#F47521",
        "description": "Самая большая библиотека аниме в мире без рекламы, серии сразу после Японии.",
        "default_plan_name": "Mega Fan",
        "popularity_rank": 13,
        "available_plans": ["Mega Fan"],
        "official_url": "https://www.crunchyroll.com",
        "guide": "Один из самых дешевых стримингов в Турции и Аргентине. Просмотр работает без VPN по всему миру.",
        "plans": [
            {
                "id": "mega-fan", "name": "Mega Fan", "period": "month", "desc": "4 экрана, офлайн-просмотр, доступ к каталогу игр.", "us_price": 9.99,
                "prices": {
                    "TR": {"amount": 65.49, "curr": "TRY", "source": "official", "avail": True, "notes": "Турецкие карты Ininal", "diff": "medium"},
                    "AR": {"amount": 2999, "curr": "ARS", "source": "official", "avail": True, "notes": "Местные аргентинские карты", "diff": "hard"},
                    "IN": {"amount": 99, "curr": "INR", "source": "official", "avail": True, "notes": "Индийские карты и UPI", "diff": "medium"},
                    "NG": {"amount": 1500, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерия", "diff": "medium"},
                    "BR": {"amount": 19.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "UA": {"amount": 3.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Биллинг в EUR", "diff": "easy"},
                    "KZ": {"amount": 3.99, "curr": "USD", "source": "official", "avail": True, "notes": "Казахстан", "diff": "easy"},
                    "PL": {"amount": 25.00, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "EG": {"amount": 69.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 119, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "JP": {"amount": 9.99, "curr": "USD", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EU": {"amount": 6.49, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 5.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 9.99, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "RU": {"amount": 299, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Остановил работу в РФ", "notes": "Crunchyroll остановил работу в РФ в марте 2022. Архивный тариф: 299 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220201000000/https://www.crunchyroll.com/ru", "date": "2022-02-01"}
                }
            }
        ]
    },
    {
        "id": "disney-plus",
        "name": "Disney+",
        "slug": "disney-plus",
        "category": "Streaming Video",
        "icon": "Tv",
        "color": "#113CCF",
        "description": "Фильмы и мультфильмы Disney, Pixar, Marvel, Star Wars, National Geographic и Star.",
        "default_plan_name": "Premium",
        "popularity_rank": 34,
        "available_plans": ["Premium"],
        "official_url": "https://www.disneyplus.com",
        "guide": "Disney+ официально не запущен в Украине и Казахстане (пользователи оформляют через Турцию или Польшу). В Индии работает под брендом Disney+ Hotstar.",
        "plans": [
            {
                "id": "premium", "name": "Premium Monthly", "period": "month", "desc": "4K UHD, HDR10, Dolby Atmos, 4 экрана.", "us_price": 13.99,
                "prices": {
                    "TR": {"amount": 134.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Турецкий регион", "diff": "medium"},
                    "IN": {"amount": 299, "curr": "INR", "source": "official", "avail": True, "notes": "Disney+ Hotstar Super", "diff": "medium"},
                    "AR": {"amount": 3999, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентина", "diff": "hard"},
                    "BR": {"amount": 33.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "PL": {"amount": 37.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "EU": {"amount": 10.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 10.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 13.99, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "JP": {"amount": 990, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EG": {"amount": 149.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет (MENA)", "diff": "medium"},
                    "PH": {"amount": 249, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "NG": {"amount": 2500, "curr": "NGN", "source": "estimated", "avail": False, "status": "not_available", "label": "Не запущен", "notes": "Официально сервис не запущен в Нигерии. Расчетная цена по региону.", "diff": "impossible"},
                    "UA": {"amount": 4.99, "curr": "USD", "source": "estimated", "avail": False, "status": "not_available", "label": "Не запущен", "notes": "Disney+ официально не запустился в Украине. Смотрят через Турцию/Польшу.", "diff": "impossible"},
                    "KZ": {"amount": 5.49, "curr": "USD", "source": "estimated", "avail": False, "status": "not_available", "label": "Не запущен", "notes": "Официально не запущен в Казахстане.", "diff": "impossible"},
                    "RU": {"amount": 399, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Ушел из РФ", "notes": "Disney ушел с рынка РФ в 2022 году.", "diff": "impossible", "url": "https://web.archive.org/web/20220201000000/https://www.disneyplus.com", "date": "2022-02-01"}
                }
            }
        ]
    },
    {
        "id": "max-hbo",
        "name": "Max (HBO Max)",
        "slug": "max-hbo",
        "category": "Streaming Video",
        "icon": "Tv",
        "color": "#002BE7",
        "description": "Фильмы Warner Bros, сериалы HBO (Игра Престолов, Одни из нас), Discovery и DC Universe.",
        "default_plan_name": "Standard",
        "popularity_rank": 35,
        "available_plans": ["Standard"],
        "official_url": "https://www.max.com",
        "guide": "Max доступен в США, Латинской Америке и некоторых странах Европы (Польша, Нидерланды). В Турции контент лицензирован сервису BluTV.",
        "plans": [
            {
                "id": "standard", "name": "Standard Monthly", "period": "month", "desc": "Full HD 1080p, 2 экрана, 30 скачиваний.", "us_price": 16.99,
                "prices": {
                    "AR": {"amount": 4299, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентина", "diff": "hard"},
                    "BR": {"amount": 34.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "PL": {"amount": 29.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "US": {"amount": 16.99, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "EU": {"amount": 9.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 9.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "JP": {"amount": 1980, "curr": "JPY", "source": "community", "avail": True, "notes": "Через сервис U-Next", "diff": "medium"},
                    "PH": {"amount": 399, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины (HBO GO)", "diff": "easy"},
                    "TR": {"amount": 99.99, "curr": "TRY", "source": "estimated", "avail": False, "status": "not_available", "label": "Через BluTV", "notes": "Контент HBO в Турции лицензирован платформе BluTV.", "diff": "impossible"},
                    "UA": {"amount": 6.99, "curr": "USD", "source": "estimated", "avail": False, "status": "not_available", "label": "Через Megogo", "notes": "Контент HBO в Украине транслируется через партнерство с Megogo.", "diff": "impossible"},
                    "KZ": {"amount": 7.49, "curr": "USD", "source": "estimated", "avail": False, "status": "not_available", "label": "Не запущен", "notes": "Официально Max в Казахстане не запущен.", "diff": "impossible"},
                    "NG": {"amount": 3500, "curr": "NGN", "source": "estimated", "avail": False, "status": "not_available", "label": "Не запущен", "notes": "Не запущен в Африке.", "diff": "impossible"},
                    "IN": {"amount": 499, "curr": "INR", "source": "estimated", "avail": False, "status": "not_available", "label": "Через JioCinema", "notes": "Контент HBO в Индии эксклюзивно доступен через JioCinema Premium.", "diff": "impossible"},
                    "EG": {"amount": 129.99, "curr": "EGP", "source": "estimated", "avail": False, "status": "not_available", "label": "Не запущен", "notes": "Не запущен.", "diff": "impossible"},
                    "RU": {"amount": 599, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Недоступен в РФ", "notes": "Контент Warner Bros / HBO отозван из РФ.", "diff": "impossible", "url": "https://web.archive.org/web/20220101000000/https://www.hbomax.com", "date": "2022-01-01"}
                }
            }
        ]
    },
    {
        "id": "apple-tv",
        "name": "Apple TV+",
        "slug": "apple-tv",
        "category": "Streaming Video",
        "icon": "Tv",
        "color": "#000000",
        "description": "Оригинальные сериалы и фильмы Apple Originals (Тед Лассо, Разделение, Утреннее шоу) в 4K Dolby Vision.",
        "default_plan_name": "Monthly",
        "popularity_rank": 36,
        "available_plans": ["Monthly"],
        "official_url": "https://tv.apple.com",
        "guide": "Оплачивается пополнением баланса Apple ID. В РФ работает оплата со счета мобильного МТС / билайн (299 ₽/мес).",
        "plans": [
            {
                "id": "monthly", "name": "Monthly Plan", "period": "month", "desc": "Полный доступ к библиотеке Apple Originals в 4K HDR.", "us_price": 9.99,
                "prices": {
                    "TR": {"amount": 59.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Турецкий Apple ID", "diff": "easy"},
                    "IN": {"amount": 99, "curr": "INR", "source": "official", "avail": True, "notes": "Индийский Apple ID", "diff": "medium"},
                    "NG": {"amount": 1400, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерийский Apple ID", "diff": "medium"},
                    "AR": {"amount": 4.99, "curr": "USD", "source": "official", "avail": True, "notes": "Аргентинский Apple ID (биллинг в USD)", "diff": "medium"},
                    "UA": {"amount": 4.99, "curr": "USD", "source": "official", "avail": True, "notes": "Украинский Apple ID", "diff": "easy"},
                    "KZ": {"amount": 4.99, "curr": "USD", "source": "official", "avail": True, "notes": "Казахстан", "diff": "easy"},
                    "BR": {"amount": 21.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "PL": {"amount": 34.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "EU": {"amount": 9.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 8.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 9.99, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "JP": {"amount": 900, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EG": {"amount": 89.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 149, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "RU": {"amount": 299, "curr": "RUB", "source": "official", "avail": True, "status": "available", "label": "Доступен", "notes": "Оплата со счета телефона МТС / билайн без ограничений.", "diff": "easy"}
                }
            }
        ]
    }
]

print("Video Services definitions loaded")
