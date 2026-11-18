# scripts/data_definitions.py
# Contains all 43 service metadata, plans, and explicit verified price overrides.

SERVICES = [
    # ==================== МУЗЫКА ====================
    {
        "id": "spotify",
        "name": "Spotify Premium",
        "slug": "spotify",
        "category": "Music",
        "icon": "Music",
        "color": "#1DB954",
        "description": "Миллионы треков без рекламы, прослушивание в высоком качестве оффлайн.",
        "default_plan_name": "Individual",
        "popularity_rank": 1,
        "available_plans": ["Individual", "Duo", "Family", "Student"],
        "official_url": "https://www.spotify.com",
        "guide": "Spotify строго проверяет совпадение региона аккаунта и страны эмитента карты. Популярные пути: индийские Gift Cards, турецкие карты Ininal или оформление через семью.",
        "plans": [
            {
                "id": "individual", "name": "Individual", "period": "month", "desc": "1 премиум аккаунт, без рекламы.", "us_price": 11.99,
                "prices": {
                    "NG": {"amount": 1300, "curr": "NGN", "source": "official", "avail": True, "notes": "Виртуальные карты Нигерии", "diff": "medium"},
                    "IN": {"amount": 119, "curr": "INR", "source": "official", "avail": True, "notes": "Легко пополняется индийскими Gift Cards", "diff": "easy"},
                    "TR": {"amount": 59.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Карты Ininal / Papara", "diff": "medium"},
                    "EG": {"amount": 89.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египетские карты", "diff": "medium"},
                    "PH": {"amount": 149, "curr": "PHP", "source": "official", "avail": True, "notes": "GCash и зарубежные карты", "diff": "easy"},
                    "AR": {"amount": 4499, "curr": "ARS", "source": "official", "avail": True, "notes": "Карты банков Аргентины (Belo, Ualá)", "diff": "hard"},
                    "BR": {"amount": 21.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразильские Gift Cards", "diff": "medium"},
                    "UA": {"amount": 4.99, "curr": "USD", "source": "official", "avail": True, "notes": "Карты банков Украины (Monobank, ПриватБанк), биллинг в USD", "diff": "easy"},
                    "KZ": {"amount": 5.49, "curr": "USD", "source": "official", "avail": True, "notes": "Карты Kaspi/Halyk, биллинг в USD", "diff": "easy"},
                    "PL": {"amount": 23.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Карты ЕС, BLIK", "diff": "easy"},
                    "JP": {"amount": 980, "curr": "JPY", "source": "official", "avail": True, "notes": "Японские карты / Gift Cards", "diff": "medium"},
                    "EU": {"amount": 10.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Карты европейских банков", "diff": "easy"},
                    "US": {"amount": 11.99, "curr": "USD", "source": "official", "avail": True, "notes": "Стандартная цена США", "diff": "easy"},
                    "GB": {"amount": 11.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Британские карты", "diff": "easy"},
                    "RU": {"amount": 169, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Ушел из РФ", "notes": "Сервис официально закрыл бизнес в РФ в апреле 2022. Архивный тариф: 169 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220201000000/https://www.spotify.com/ru-ru/premium/", "date": "2022-02-01"}
                }
            },
            {
                "id": "family", "name": "Family", "period": "month", "desc": "До 6 аккаунтов для членов семьи.", "us_price": 19.99,
                "prices": {
                    "NG": {"amount": 2100, "curr": "NGN", "source": "official", "avail": True, "notes": "Виртуальные карты Нигерии", "diff": "medium"},
                    "IN": {"amount": 179, "curr": "INR", "source": "official", "avail": True, "notes": "Индийские подарочные карты", "diff": "easy"},
                    "TR": {"amount": 99.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Карты Ininal / Papara", "diff": "medium"},
                    "EG": {"amount": 149.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египетские карты", "diff": "medium"},
                    "PH": {"amount": 239, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппинские карты", "diff": "easy"},
                    "AR": {"amount": 7599, "curr": "ARS", "source": "official", "avail": True, "notes": "Местные аргентинские карты", "diff": "hard"},
                    "BR": {"amount": 34.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразильские карты", "diff": "medium"},
                    "UA": {"amount": 7.99, "curr": "USD", "source": "official", "avail": True, "notes": "Карты банков Украины (Monobank, ПриватБанк), биллинг в USD", "diff": "easy"},
                    "KZ": {"amount": 8.99, "curr": "USD", "source": "official", "avail": True, "notes": "Карты Казахстана, биллинг в USD", "diff": "easy"},
                    "PL": {"amount": 37.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Карты Польши", "diff": "easy"},
                    "JP": {"amount": 1580, "curr": "JPY", "source": "official", "avail": True, "notes": "Японские карты", "diff": "medium"},
                    "EU": {"amount": 17.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Карты европейских банков", "diff": "easy"},
                    "US": {"amount": 19.99, "curr": "USD", "source": "official", "avail": True, "notes": "Стандартная цена США", "diff": "easy"},
                    "GB": {"amount": 19.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Британские карты", "diff": "easy"},
                    "RU": {"amount": 269, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Ушел из РФ", "notes": "Сервис закрыл бизнес в РФ. Архивный тариф: 269 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220201000000/https://www.spotify.com/ru-ru/premium/", "date": "2022-02-01"}
                }
            }
        ]
    },
    {
        "id": "apple-music",
        "name": "Apple Music",
        "slug": "apple-music",
        "category": "Music",
        "icon": "Disc",
        "color": "#FA2D48",
        "description": "Более 100 млн треков в Lossless Audio и Spatial Audio с Dolby Atmos.",
        "default_plan_name": "Individual",
        "popularity_rank": 2,
        "available_plans": ["Individual", "Family", "Student"],
        "official_url": "https://music.apple.com",
        "guide": "Оплачивается пополнением баланса Apple ID через официальные Gift Card региона (Турция, США). В РФ работает оплата со счета мобильного телефона МТС/билайн.",
        "plans": [
            {
                "id": "individual", "name": "Individual", "period": "month", "desc": "Индивидуальная подписка с Lossless качеством.", "us_price": 10.99,
                "prices": {
                    "NG": {"amount": 1000, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерийский Apple ID", "diff": "medium"},
                    "TR": {"amount": 39.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Пополнение через Apple Gift Card TR", "diff": "easy"},
                    "IN": {"amount": 99, "curr": "INR", "source": "official", "avail": True, "notes": "Индийский Apple ID", "diff": "medium"},
                    "EG": {"amount": 79.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египетский Apple ID", "diff": "medium"},
                    "PH": {"amount": 139, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппинский Apple ID", "diff": "easy"},
                    "AR": {"amount": 3.49, "curr": "USD", "source": "official", "avail": True, "notes": "Apple ID Аргентина, биллинг в USD", "diff": "medium"},
                    "BR": {"amount": 21.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразильский Apple ID", "diff": "medium"},
                    "UA": {"amount": 4.99, "curr": "USD", "source": "official", "avail": True, "notes": "Украинские карты, биллинг в USD", "diff": "easy"},
                    "KZ": {"amount": 2.99, "curr": "USD", "source": "official", "avail": True, "notes": "Карты Казахстана", "diff": "easy"},
                    "PL": {"amount": 21.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Карты ЕС", "diff": "easy"},
                    "JP": {"amount": 1080, "curr": "JPY", "source": "official", "avail": True, "notes": "Apple Gift Card JP", "diff": "medium"},
                    "EU": {"amount": 10.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Европейский Apple ID", "diff": "easy"},
                    "US": {"amount": 10.99, "curr": "USD", "source": "official", "avail": True, "notes": "Базовая цена США", "diff": "easy"},
                    "GB": {"amount": 10.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Британский Apple ID", "diff": "easy"},
                    "RU": {"amount": 169, "curr": "RUB", "source": "official", "avail": True, "status": "available", "label": "Доступен", "notes": "Оплата со счета МТС / билайн без комиссии", "diff": "easy"}
                }
            }
        ]
    },
    {
        "id": "soundcloud",
        "name": "SoundCloud Go+",
        "slug": "soundcloud",
        "category": "Music",
        "icon": "Radio",
        "color": "#FF5500",
        "description": "Эксклюзивные диджей-сеты, ремиксы, треки без рекламы и оффлайн-режим в высоком битрейте.",
        "default_plan_name": "Go+ Monthly",
        "popularity_rank": 3,
        "available_plans": ["Go", "Go+ Monthly"],
        "official_url": "https://soundcloud.com/go",
        "guide": "Один из флагманских товаров на Spoteeq. Выгоднее всего подключать через Турцию или Нигерию через мобильное приложение App Store / Google Play.",
        "plans": [
            {
                "id": "goplus", "name": "Go+ Monthly", "period": "month", "desc": "Полный каталог треков и диджейских сетов без ограничений.", "us_price": 9.99,
                "prices": {
                    "NG": {"amount": 2200, "curr": "NGN", "source": "store", "avail": True, "notes": "Через Google Play Нигерии", "diff": "medium"},
                    "TR": {"amount": 89.99, "curr": "TRY", "source": "store", "avail": True, "notes": "Через турецкий Apple ID", "diff": "easy"},
                    "IN": {"amount": 149, "curr": "INR", "source": "store", "avail": True, "notes": "Индийский Google Play / App Store", "diff": "medium"},
                    "EG": {"amount": 119.99, "curr": "EGP", "source": "store", "avail": True, "notes": "Google Play Египет", "diff": "medium"},
                    "PH": {"amount": 199, "curr": "PHP", "source": "store", "avail": True, "notes": "Google Play Филиппины", "diff": "easy"},
                    "AR": {"amount": 1999, "curr": "ARS", "source": "community", "avail": True, "notes": "Аргентинский аккаунт", "diff": "hard"},
                    "BR": {"amount": 19.90, "curr": "BRL", "source": "store", "avail": True, "notes": "App Store Бразилия", "diff": "medium"},
                    "UA": {"amount": 4.99, "curr": "USD", "source": "official", "avail": True, "notes": "Биллинг в USD", "diff": "easy"},
                    "KZ": {"amount": 4.99, "curr": "USD", "source": "official", "avail": True, "notes": "Карты Казахстана", "diff": "easy"},
                    "PL": {"amount": 23.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Европейские карты", "diff": "easy"},
                    "JP": {"amount": 980, "curr": "JPY", "source": "official", "avail": True, "notes": "Японские карты", "diff": "medium"},
                    "EU": {"amount": 9.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Карты ЕС", "diff": "easy"},
                    "US": {"amount": 9.99, "curr": "USD", "source": "official", "avail": True, "notes": "Стандартная цена США", "diff": "easy"},
                    "GB": {"amount": 9.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Карты Великобритании", "diff": "easy"},
                    "RU": {"amount": 169, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Заблокирован в РФ", "notes": "SoundCloud заблокирован Роскомнадзором. Архивный тариф: 169 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220101000000/https://soundcloud.com/go", "date": "2022-01-01"}
                }
            }
        ]
    },
    {
        "id": "deezer",
        "name": "Deezer Premium",
        "slug": "deezer",
        "category": "Music",
        "icon": "Disc",
        "color": "#A238FF",
        "description": "Высокое качество звука FLAC HiFi, Flow и персональные плейлисты.",
        "default_plan_name": "Premium",
        "popularity_rank": 4,
        "available_plans": ["Premium", "Family"],
        "official_url": "https://www.deezer.com",
        "guide": "Deezer доступен во многих странах с сильными региональными скидками в Турции и Бразилии.",
        "plans": [
            {
                "id": "premium", "name": "Premium", "period": "month", "desc": "FLAC 16-бит 44.1 кГц без рекламы.", "us_price": 10.99,
                "prices": {
                    "TR": {"amount": 42.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Турецкая карта Ininal", "diff": "medium"},
                    "NG": {"amount": 1200, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерийский биллинг", "diff": "medium"},
                    "IN": {"amount": 119, "curr": "INR", "source": "official", "avail": True, "notes": "Индийские карты", "diff": "easy"},
                    "EG": {"amount": 89.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египетские карты", "diff": "medium"},
                    "PH": {"amount": 149, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "AR": {"amount": 2499, "curr": "ARS", "source": "official", "avail": True, "notes": "Карты Аргентины", "diff": "hard"},
                    "BR": {"amount": 22.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразильские карты", "diff": "medium"},
                    "UA": {"amount": 4.99, "curr": "USD", "source": "official", "avail": True, "notes": "Биллинг в USD", "diff": "easy"},
                    "KZ": {"amount": 5.99, "curr": "USD", "source": "official", "avail": True, "notes": "Карты Казахстана", "diff": "easy"},
                    "PL": {"amount": 21.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Карты ЕС", "diff": "easy"},
                    "JP": {"amount": 1080, "curr": "JPY", "source": "official", "avail": True, "notes": "Карты Японии", "diff": "medium"},
                    "EU": {"amount": 10.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Карты ЕС", "diff": "easy"},
                    "US": {"amount": 10.99, "curr": "USD", "source": "official", "avail": True, "notes": "Стандартная цена США", "diff": "easy"},
                    "GB": {"amount": 11.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Британские карты", "diff": "easy"},
                    "RU": {"amount": 169, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Ушел из РФ", "notes": "Deezer закрыл бизнес в РФ. Архивный тариф: 169 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220110000000/https://www.deezer.com/ru/offers", "date": "2022-01-10"}
                }
            }
        ]
    },
    {
        "id": "tidal",
        "name": "Tidal HiFi",
        "slug": "tidal",
        "category": "Music",
        "icon": "Disc",
        "color": "#000000",
        "description": "Hi-Res FLAC до 24 бит, 192 кГц и Dolby Atmos для аудиофилов.",
        "default_plan_name": "HiFi Individual",
        "popularity_rank": 30,
        "available_plans": ["HiFi Individual"],
        "official_url": "https://tidal.com",
        "guide": "Tidal ушел из Турции из-за требований регулятора RTUK. Выгодные регионы: Аргентина, Бразилия, Нигерия.",
        "plans": [
            {
                "id": "individual", "name": "HiFi Individual", "period": "month", "desc": "Hi-Res FLAC 24-bit 192kHz.", "us_price": 10.99,
                "prices": {
                    "AR": {"amount": 1999, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентинские карты", "diff": "hard"},
                    "NG": {"amount": 1200, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерия", "diff": "medium"},
                    "BR": {"amount": 21.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "PL": {"amount": 21.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "UA": {"amount": 4.99, "curr": "USD", "source": "official", "avail": True, "notes": "Биллинг в USD", "diff": "easy"},
                    "KZ": {"amount": 5.49, "curr": "USD", "source": "official", "avail": True, "notes": "Казахстан", "diff": "easy"},
                    "IN": {"amount": 149, "curr": "INR", "source": "community", "avail": True, "notes": "Индия", "diff": "medium"},
                    "EG": {"amount": 89.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 149, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "EU": {"amount": 10.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 10.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 10.99, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "JP": {"amount": 1080, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "TR": {"amount": 39.99, "curr": "TRY", "source": "archive", "avail": False, "status": "suspended", "label": "Ушел из Турции", "notes": "Tidal ушел из Турции из-за RTUK. Архивный тариф: 39.99 TRY.", "diff": "impossible", "url": "https://web.archive.org/web/20220801000000/https://tidal.com/pricing", "date": "2022-08-01"},
                    "RU": {"amount": 9.99, "curr": "USD", "source": "archive", "avail": False, "status": "suspended", "label": "Недоступен в РФ", "notes": "Никогда официально не запускался в РФ.", "diff": "impossible", "url": "https://web.archive.org/web/20220101000000/https://tidal.com/", "date": "2022-01-01"}
                }
            }
        ]
    },
    {
        "id": "splice",
        "name": "Splice Sounds",
        "slug": "splice",
        "category": "Music & Audio",
        "icon": "Sliders",
        "color": "#001FFF",
        "description": "Крупнейшая библиотека роялти-фри сэмплов, лупов, плагинов и пресетов для музыкантов.",
        "default_plan_name": "Sounds 100",
        "popularity_rank": 31,
        "available_plans": ["Sounds 100"],
        "official_url": "https://splice.com",
        "guide": "Splice использует глобальную фиксированную цену в долларах США ($12.99/мес). Оплата требует зарубежную карту.",
        "is_global_usd": True,
        "plans": [
            {
                "id": "sounds-100", "name": "Sounds 100", "period": "month", "desc": "100 сэмпл-кредитов ежемесячно.", "us_price": 12.99,
                "prices": {
                    "US": {"amount": 12.99, "curr": "USD", "source": "official", "avail": True, "notes": "Базовая цена США", "diff": "easy"},
                    "RU": {"amount": 12.99, "curr": "USD", "source": "usd_flat", "avail": False, "status": "suspended", "label": "Блокировка карт РФ", "notes": "Прямая оплата картами РФ не проходит.", "diff": "impossible"}
                }
            }
        ]
    }
]

print("Batch 1 (Music) definitions loaded")
