# scripts/data_gaming.py
# Gaming and Interactive Entertainment services

GAMING_SERVICES = [
    {
        "id": "playstation-plus",
        "name": "PlayStation Plus Deluxe",
        "slug": "playstation-plus",
        "category": "Gaming",
        "icon": "Gamepad2",
        "color": "#003791",
        "description": "Сотни игр из каталога PS4/PS5, классика PS1/PS2/PSP, облачный стриминг и сетевая игра.",
        "default_plan_name": "Deluxe Monthly",
        "popularity_rank": 19,
        "available_plans": ["Deluxe Monthly"],
        "official_url": "https://www.playstation.com/ps-plus",
        "guide": "Турция и Украина — два главных региона для игроков из СНГ. Турецкий PSN пополняется картами Ininal / Ozan / турецкими Gift Card. Украинский PSN принимает карты украинских банков.",
        "plans": [
            {
                "id": "deluxe-monthly", "name": "Deluxe Monthly", "period": "month", "desc": "Максимальный тариф: каталог игр + классика + пробы игр.", "us_price": 17.99,
                "prices": {
                    "TR": {"amount": 460.00, "curr": "TRY", "source": "official", "avail": True, "notes": "Турецкий PSN Store", "diff": "medium"},
                    "IN": {"amount": 849, "curr": "INR", "source": "official", "avail": True, "notes": "Индийский PSN", "diff": "medium"},
                    "UA": {"amount": 369, "curr": "UAH", "source": "official", "avail": True, "notes": "Украинский PSN Store", "diff": "easy"},
                    "PL": {"amount": 68.00, "curr": "PLN", "source": "official", "avail": True, "notes": "Польский PSN", "diff": "easy"},
                    "BR": {"amount": 59.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразильский PSN", "diff": "medium"},
                    "JP": {"amount": 1550, "curr": "JPY", "source": "official", "avail": True, "notes": "Японский PSN", "diff": "medium"},
                    "EU": {"amount": 16.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Европейский PSN", "diff": "easy"},
                    "GB": {"amount": 13.49, "curr": "GBP", "source": "official", "avail": True, "notes": "Британский PSN", "diff": "easy"},
                    "US": {"amount": 17.99, "curr": "USD", "source": "official", "avail": True, "notes": "Американский PSN (Premium)", "diff": "easy"},
                    "AR": {"amount": 17.99, "curr": "USD", "source": "official", "avail": True, "notes": "Аргентинский PSN (биллинг в USD)", "diff": "hard"},
                    "EG": {"amount": 17.99, "curr": "USD", "source": "official", "avail": True, "notes": "Египет (MENA регион в USD)", "diff": "medium"},
                    "PH": {"amount": 790, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины / Азия", "diff": "easy"},
                    "KZ": {"amount": 6500, "curr": "KZT", "source": "estimated", "avail": False, "status": "not_available", "label": "Нет своего PSN", "notes": "Sony не открыла PS Store в Казахстане. Игроки создают аккаунты региона UA, TR или US.", "diff": "impossible"},
                    "NG": {"amount": 8500, "curr": "NGN", "source": "estimated", "avail": False, "status": "not_available", "label": "Нет своего PSN", "notes": "В Нигерии нет регионального PS Store.", "diff": "impossible"},
                    "RU": {"amount": 529, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "PS Store заморожен", "notes": "Sony закрыла продажи в РФ в марте 2022. Архивный тариф: 529 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220201000000/https://store.playstation.com/ru-ru/", "date": "2022-02-01"}
                }
            }
        ]
    },
    {
        "id": "xbox-game-pass",
        "name": "Xbox Game Pass Ultimate",
        "slug": "xbox-game-pass",
        "category": "Gaming",
        "icon": "Box",
        "color": "#107C10",
        "description": "Сотни игр для консолей Xbox и ПК, новинки в день релиза, EA Play и Xbox Cloud Gaming.",
        "default_plan_name": "Ultimate",
        "popularity_rank": 20,
        "available_plans": ["Ultimate"],
        "official_url": "https://www.xbox.com/game-pass",
        "guide": "Синхронизируется напрямую с Microsoft Store DisplayCatalog API. Самые выгодные регионы: Турция, Индия, Бразилия.",
        "plans": [
            {
                "id": "ultimate", "name": "Ultimate", "period": "month", "desc": "Консоли Xbox + ПК + EA Play + Cloud Gaming.", "us_price": 19.99,
                "prices": {
                    "TR": {"amount": 529.00, "curr": "TRY", "source": "official", "avail": True, "notes": "Официальный Microsoft Store TR API", "diff": "medium"},
                    "IN": {"amount": 549, "curr": "INR", "source": "official", "avail": True, "notes": "Индийский MS Store", "diff": "medium"},
                    "BR": {"amount": 49.99, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразильский MS Store", "diff": "medium"},
                    "PL": {"amount": 69.00, "curr": "PLN", "source": "official", "avail": True, "notes": "Польский MS Store", "diff": "easy"},
                    "UA": {"amount": 399, "curr": "UAH", "source": "official", "avail": True, "notes": "Украинский регион Xbox", "diff": "easy"},
                    "AR": {"amount": 8999, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентина", "diff": "hard"},
                    "NG": {"amount": 3500, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерия", "diff": "medium"},
                    "KZ": {"amount": 16.99, "curr": "USD", "source": "official", "avail": True, "notes": "Казахстан (биллинг в USD)", "diff": "easy"},
                    "JP": {"amount": 1450, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EU": {"amount": 14.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 12.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 19.99, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "EG": {"amount": 289.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 790, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины (PC Game Pass / Ultimate)", "diff": "easy"},
                    "RU": {"amount": 899, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Продажи остановлены", "notes": "Microsoft остановил прямые продажи в РФ в 2022. Архивный тариф: 899 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220201000000/https://www.xbox.com/ru-ru/xbox-game-pass", "date": "2022-02-01"}
                }
            }
        ]
    },
    {
        "id": "steam-ea-play",
        "name": "Steam EA Play",
        "slug": "steam-ea-play",
        "category": "Gaming",
        "icon": "Gamepad",
        "color": "#171A21",
        "description": "Каталог топовых игр EA (Battlefield, FIFA/FC, Need for Speed, Mass Effect, Dead Space) в Steam.",
        "default_plan_name": "Monthly",
        "popularity_rank": 21,
        "available_plans": ["Monthly"],
        "official_url": "https://store.steampowered.com/subscriptions/ea",
        "guide": "Синхронизируется напрямую с Steam Store API (AppID 1289670). Пополняется кошельками Steam соответствующего региона.",
        "plans": [
            {
                "id": "monthly", "name": "EA Play Monthly", "period": "month", "desc": "Доступ к The Play List, 10% скидка на покупки EA, ранние пробы.", "us_price": 5.99,
                "prices": {
                    "UA": {"amount": 149, "curr": "UAH", "source": "store", "avail": True, "notes": "Steam Store UA API", "diff": "easy"},
                    "KZ": {"amount": 1999, "curr": "KZT", "source": "store", "avail": True, "notes": "Steam Store KZ API", "diff": "easy"},
                    "IN": {"amount": 315, "curr": "INR", "source": "store", "avail": True, "notes": "Steam Store IN API", "diff": "medium"},
                    "BR": {"amount": 19.90, "curr": "BRL", "source": "store", "avail": True, "notes": "Steam Store BR API", "diff": "medium"},
                    "PL": {"amount": 24.99, "curr": "PLN", "source": "store", "avail": True, "notes": "Steam Store PL API", "diff": "easy"},
                    "TR": {"amount": 5.99, "curr": "USD", "source": "store", "avail": True, "notes": "Steam Store TR (MENA-USD)", "diff": "medium"},
                    "AR": {"amount": 5.99, "curr": "USD", "source": "store", "avail": True, "notes": "Steam Store AR (LATAM-USD)", "diff": "hard"},
                    "NG": {"amount": 5.99, "curr": "USD", "source": "store", "avail": True, "notes": "Steam Store NG (Global USD)", "diff": "medium"},
                    "US": {"amount": 5.99, "curr": "USD", "source": "store", "avail": True, "notes": "Steam Store US", "diff": "easy"},
                    "EU": {"amount": 5.99, "curr": "EUR", "source": "store", "avail": True, "notes": "Steam Store EU", "diff": "easy"},
                    "GB": {"amount": 4.99, "curr": "GBP", "source": "store", "avail": True, "notes": "Steam Store GB", "diff": "easy"},
                    "JP": {"amount": 528, "curr": "JPY", "source": "store", "avail": True, "notes": "Steam Store JP", "diff": "medium"},
                    "EG": {"amount": 5.99, "curr": "USD", "source": "store", "avail": True, "notes": "Steam Store EG (MENA-USD)", "diff": "medium"},
                    "PH": {"amount": 179, "curr": "PHP", "source": "store", "avail": True, "notes": "Steam Store PH", "diff": "easy"},
                    "RU": {"amount": 299, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Снято с продажи в РФ", "notes": "EA сняла свои подписки и игры с продажи в Steam РФ в марте 2022. Архивный тариф: 299 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220201000000/https://store.steampowered.com/subscriptions/ea", "date": "2022-02-01"}
                }
            }
        ]
    },
    {
        "id": "nintendo-switch-online",
        "name": "Nintendo Switch Online",
        "slug": "nintendo-switch-online",
        "category": "Gaming",
        "icon": "Gamepad2",
        "color": "#E60012",
        "description": "Сетевая игра на Switch, облачные сохранения и библиотека ретро-игр NES, SNES, Game Boy.",
        "default_plan_name": "12 Months Individual",
        "popularity_rank": 22,
        "available_plans": ["12 Months Individual"],
        "official_url": "https://www.nintendo.com/switch/online",
        "guide": "В Аргентине, Бразилии и Японии выгодные годовые цены. В Турции и Украине официального eShop нет, игроки выбирают регион Польша или США.",
        "plans": [
            {
                "id": "individual-year", "name": "12 Months Individual", "period": "year", "desc": "12 месяцев сетевой игры, облачные сейвы, каталог NES/SNES.", "us_price": 19.99,
                "prices": {
                    "AR": {"amount": 3999, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентинский Nintendo eShop", "diff": "hard"},
                    "BR": {"amount": 100.00, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразильский eShop", "diff": "medium"},
                    "JP": {"amount": 2400, "curr": "JPY", "source": "official", "avail": True, "notes": "Японский eShop", "diff": "medium"},
                    "PL": {"amount": 80.00, "curr": "PLN", "source": "official", "avail": True, "notes": "Польский eShop", "diff": "easy"},
                    "EU": {"amount": 19.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Европейский eShop", "diff": "easy"},
                    "GB": {"amount": 17.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Британский eShop", "diff": "easy"},
                    "US": {"amount": 19.99, "curr": "USD", "source": "official", "avail": True, "notes": "Американский eShop", "diff": "easy"},
                    "TR": {"amount": 349.00, "curr": "TRY", "source": "estimated", "avail": False, "status": "not_available", "label": "Нет своего eShop", "notes": "В Турции нет eShop. Покупают в Польше или ЮАР.", "diff": "impossible"},
                    "UA": {"amount": 399, "curr": "UAH", "source": "estimated", "avail": False, "status": "not_available", "label": "Нет своего eShop", "notes": "В Украине нет eShop. Используют Польшу/США.", "diff": "impossible"},
                    "KZ": {"amount": 4900, "curr": "KZT", "source": "estimated", "avail": False, "status": "not_available", "label": "Нет своего eShop", "notes": "В Казахстане нет eShop.", "diff": "impossible"},
                    "NG": {"amount": 7500, "curr": "NGN", "source": "estimated", "avail": False, "status": "not_available", "label": "Нет своего eShop", "notes": "В Нигерии нет eShop.", "diff": "impossible"},
                    "IN": {"amount": 799, "curr": "INR", "source": "estimated", "avail": False, "status": "not_available", "label": "Нет своего eShop", "notes": "В Индии нет eShop.", "diff": "impossible"},
                    "EG": {"amount": 19.99, "curr": "USD", "source": "estimated", "avail": False, "status": "not_available", "label": "Не запущен", "notes": "Нет eShop.", "diff": "impossible"},
                    "PH": {"amount": 599, "curr": "PHP", "source": "estimated", "avail": False, "status": "not_available", "label": "Не запущен", "notes": "Нет eShop.", "diff": "impossible"},
                    "RU": {"amount": 1399, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "eShop закрыт", "notes": "Nintendo eShop в РФ закрыт на бессрочное обслуживание. Архивный тариф: 1399 ₽/год.", "diff": "impossible", "url": "https://web.archive.org/web/20220210000000/https://www.nintendo.ru/switch/online", "date": "2022-02-10"}
                }
            }
        ]
    },
    {
        "id": "roblox-premium",
        "name": "Roblox Premium 1000",
        "slug": "roblox-premium",
        "category": "Gaming",
        "icon": "Box",
        "color": "#000000",
        "description": "Ежемесячные 1000 Robux, доступ к торговле вещами и 10% бонус при покупке Robux.",
        "default_plan_name": "Premium 1000",
        "popularity_rank": 37,
        "available_plans": ["Premium 1000"],
        "official_url": "https://www.roblox.com/premium/membership",
        "guide": "В Турции, Аргентине и Индии стоимость подписки существенно ниже стандартных $9.99/мес. В РФ покупка возможна через мобильные платежи или Gift Card.",
        "plans": [
            {
                "id": "premium-1000", "name": "Premium 1000", "period": "month", "desc": "1,000 Robux каждый месяц, трейдинг предметов.", "us_price": 9.99,
                "prices": {
                    "TR": {"amount": 189.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Турецкий регион", "diff": "medium"},
                    "AR": {"amount": 4999, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентина", "diff": "hard"},
                    "IN": {"amount": 899, "curr": "INR", "source": "official", "avail": True, "notes": "Индия", "diff": "easy"},
                    "NG": {"amount": 4500, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерия", "diff": "medium"},
                    "UA": {"amount": 9.99, "curr": "USD", "source": "official", "avail": True, "notes": "Биллинг в USD", "diff": "easy"},
                    "KZ": {"amount": 9.99, "curr": "USD", "source": "official", "avail": True, "notes": "Биллинг в USD", "diff": "easy"},
                    "BR": {"amount": 54.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "PL": {"amount": 49.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "EU": {"amount": 9.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 8.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 9.99, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "JP": {"amount": 1200, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EG": {"amount": 199.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 499, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "RU": {"amount": 999, "curr": "RUB", "source": "store", "avail": True, "status": "available", "label": "Доступен", "notes": "Оплата через баланс App Store (МТС/билайн) или Google Play Gift Card.", "diff": "easy"}
                }
            }
        ]
    }
]

print("Gaming Services definitions loaded")
