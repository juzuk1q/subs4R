# scripts/data_productivity.py
# Productivity, Design, Dev, Security & Social services (17 services)

PRODUCTIVITY_SERVICES = [
    {
        "id": "adobe-creative-cloud",
        "name": "Adobe Creative Cloud",
        "slug": "adobe-creative-cloud",
        "category": "Design & Creativity",
        "icon": "Palette",
        "color": "#FF0000",
        "description": "Полный пакет Photoshop, Illustrator, Premiere Pro, After Effects и 100 ГБ облака.",
        "default_plan_name": "All Apps",
        "popularity_rank": 14,
        "available_plans": ["All Apps"],
        "official_url": "https://www.adobe.com/creativecloud.html",
        "guide": "В Турции, Аргентине и Индии действуют сильные региональные скидки. В РФ официальные продажи прекращены.",
        "plans": [
            {
                "id": "all-apps", "name": "All Apps", "period": "month", "desc": "Более 20 профессиональных приложений Adobe.", "us_price": 54.99,
                "prices": {
                    "TR": {"amount": 777.00, "curr": "TRY", "source": "official", "avail": True, "notes": "Турецкий регион Adobe", "diff": "medium"},
                    "AR": {"amount": 19999, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентина", "diff": "hard"},
                    "IN": {"amount": 2399, "curr": "INR", "source": "official", "avail": True, "notes": "Индия", "diff": "easy"},
                    "NG": {"amount": 15000, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерия", "diff": "medium"},
                    "BR": {"amount": 275.00, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "UA": {"amount": 35.99, "curr": "USD", "source": "official", "avail": True, "notes": "Украинский регион (USD)", "diff": "easy"},
                    "KZ": {"amount": 39.99, "curr": "USD", "source": "official", "avail": True, "notes": "Казахстан (USD)", "diff": "easy"},
                    "PL": {"amount": 279.00, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "EU": {"amount": 64.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 54.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 54.99, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "JP": {"amount": 6480, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EG": {"amount": 899.00, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 2650, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "RU": {"amount": 3200, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Продажи прекращены", "notes": "Adobe прекратила продажи в РФ в марте 2022. Архивный тариф: 3200 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220201000000/https://www.adobe.com/ru/creativecloud.html", "date": "2022-02-01"}
                }
            }
        ]
    },
    {
        "id": "canva-pro",
        "name": "Canva Pro",
        "slug": "canva-pro",
        "category": "Design & Creativity",
        "icon": "Sparkles",
        "color": "#00C4CC",
        "description": "Премиум-шаблоны, удаление фона в один клик, Brand Kit и 1 ТБ облачного хранилища.",
        "default_plan_name": "Pro Monthly",
        "popularity_rank": 15,
        "available_plans": ["Pro Monthly"],
        "official_url": "https://www.canva.com/pro",
        "guide": "В Турции, Индии и Нигерии Canva Pro продается с огромными скидками относительно цены США ($12.99).",
        "plans": [
            {
                "id": "pro-monthly", "name": "Pro Monthly", "period": "month", "desc": "100+ млн премиум-фото, векторных иконок, аудио и видео.", "us_price": 12.99,
                "prices": {
                    "TR": {"amount": 84.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Турецкий биллинг", "diff": "medium"},
                    "IN": {"amount": 499, "curr": "INR", "source": "official", "avail": True, "notes": "Индия", "diff": "easy"},
                    "AR": {"amount": 3999, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентина", "diff": "hard"},
                    "NG": {"amount": 2800, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерия", "diff": "medium"},
                    "BR": {"amount": 34.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "UA": {"amount": 6.99, "curr": "USD", "source": "official", "avail": True, "notes": "Украина", "diff": "easy"},
                    "KZ": {"amount": 7.99, "curr": "USD", "source": "official", "avail": True, "notes": "Казахстан", "diff": "easy"},
                    "PL": {"amount": 49.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "EU": {"amount": 11.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 10.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 12.99, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "JP": {"amount": 1500, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EG": {"amount": 129.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 299, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "RU": {"amount": 499, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Заблокирована в РФ", "notes": "Canva заблокирована Роскомнадзором в июне 2022. Архивный тариф: 499 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220201000000/https://www.canva.com/ru_ru/pricing/", "date": "2022-02-01"}
                }
            }
        ]
    },
    {
        "id": "microsoft-365",
        "name": "Microsoft 365",
        "slug": "microsoft-365",
        "category": "Productivity",
        "icon": "FileText",
        "color": "#D83B01",
        "description": "Word, Excel, PowerPoint, Outlook и 1 ТБ в облачном хранилище OneDrive.",
        "default_plan_name": "Personal Monthly",
        "popularity_rank": 16,
        "available_plans": ["Personal Monthly"],
        "official_url": "https://www.microsoft.com/microsoft-365",
        "guide": "Прямая синхронизация с Microsoft Store DisplayCatalog API. Самый дешевый регион — Турция.",
        "plans": [
            {
                "id": "personal-monthly", "name": "Personal Monthly", "period": "month", "desc": "1 пользователь, 5 устройств одновременно, 1 ТБ OneDrive.", "us_price": 6.99,
                "prices": {
                    "TR": {"amount": 159.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Microsoft Store TR", "diff": "medium"},
                    "IN": {"amount": 489, "curr": "INR", "source": "official", "avail": True, "notes": "Индия", "diff": "easy"},
                    "NG": {"amount": 3200, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерия", "diff": "medium"},
                    "AR": {"amount": 4999, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентина", "diff": "hard"},
                    "BR": {"amount": 36.00, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "UA": {"amount": 189, "curr": "UAH", "source": "official", "avail": True, "notes": "Украина", "diff": "easy"},
                    "KZ": {"amount": 2699, "curr": "KZT", "source": "official", "avail": True, "notes": "Казахстан", "diff": "easy"},
                    "PL": {"amount": 29.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "EU": {"amount": 7.00, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 5.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 6.99, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "JP": {"amount": 1284, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EG": {"amount": 119.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 349, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "RU": {"amount": 269, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Продажи остановлены", "notes": "Microsoft остановил прямые продажи в РФ. Архивный тариф: 269 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220201000000/https://www.microsoft.com/ru-ru/microsoft-365", "date": "2022-02-01"}
                }
            }
        ]
    },
    {
        "id": "zoom-pro",
        "name": "Zoom Pro",
        "slug": "zoom-pro",
        "category": "Productivity",
        "icon": "Video",
        "color": "#0B5CFF",
        "description": "Снятие 40-минутного лимита, конференции до 100 участников, 5 ГБ облачной записи.",
        "default_plan_name": "Pro Monthly",
        "popularity_rank": 17,
        "available_plans": ["Pro Monthly"],
        "official_url": "https://zoom.us/pricing",
        "guide": "Глобальный прайс в долларах ($15.99/мес). Оплата зарубежными картами.",
        "is_global_usd": True,
        "plans": [
            {
                "id": "pro-monthly", "name": "Pro Monthly", "period": "month", "desc": "Конференции до 30 часов, запись в облако.", "us_price": 15.99,
                "prices": {
                    "US": {"amount": 15.99, "curr": "USD", "source": "official", "avail": True, "notes": "Базовая цена", "diff": "easy"},
                    "EU": {"amount": 13.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "RU": {"amount": 15.99, "curr": "USD", "source": "usd_flat", "avail": False, "status": "suspended", "label": "Ограничено в РФ", "notes": "Zoom ограничил продажу лицензий клиентам из РФ.", "diff": "impossible"}
                }
            }
        ]
    },
    {
        "id": "duolingo-super",
        "name": "Duolingo Super",
        "slug": "duolingo-super",
        "category": "Education",
        "icon": "GraduationCap",
        "color": "#58CC02",
        "description": "Изучение языков без рекламы, бесконечные жизни и персонализированная практика ошибок.",
        "default_plan_name": "Super Monthly",
        "popularity_rank": 18,
        "available_plans": ["Super Monthly"],
        "official_url": "https://www.duolingo.com/super",
        "guide": "В Турции, Аргентине и Индии стоимость подписки через мобильные сторы App Store / Google Play в 4–5 раз дешевле цены США.",
        "plans": [
            {
                "id": "super-monthly", "name": "Super Monthly", "period": "month", "desc": "Безлимитные жизни, тест на уровень, отсутствие рекламы.", "us_price": 12.99,
                "prices": {
                    "TR": {"amount": 49.99, "curr": "TRY", "source": "store", "avail": True, "notes": "Через турецкий App Store / Google Play", "diff": "easy"},
                    "IN": {"amount": 199, "curr": "INR", "source": "store", "avail": True, "notes": "Индия", "diff": "medium"},
                    "AR": {"amount": 2499, "curr": "ARS", "source": "store", "avail": True, "notes": "Аргентина", "diff": "hard"},
                    "NG": {"amount": 1800, "curr": "NGN", "source": "store", "avail": True, "notes": "Нигерия", "diff": "medium"},
                    "BR": {"amount": 29.90, "curr": "BRL", "source": "store", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "UA": {"amount": 4.99, "curr": "USD", "source": "store", "avail": True, "notes": "Украина", "diff": "easy"},
                    "KZ": {"amount": 5.49, "curr": "USD", "source": "store", "avail": True, "notes": "Казахстан", "diff": "easy"},
                    "PL": {"amount": 31.99, "curr": "PLN", "source": "store", "avail": True, "notes": "Польша", "diff": "easy"},
                    "EU": {"amount": 10.99, "curr": "EUR", "source": "store", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 9.99, "curr": "GBP", "source": "store", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 12.99, "curr": "USD", "source": "store", "avail": True, "notes": "США", "diff": "easy"},
                    "JP": {"amount": 1200, "curr": "JPY", "source": "store", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EG": {"amount": 89.99, "curr": "EGP", "source": "store", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 199, "curr": "PHP", "source": "store", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "RU": {"amount": 299, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Оплата отключена", "notes": "Google Play и App Store отключили внутренние покупки в РФ. Архивный тариф: 299 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220201000000/https://www.duolingo.com", "date": "2022-02-01"}
                }
            }
        ]
    },
    {
        "id": "telegram-premium",
        "name": "Telegram Premium",
        "slug": "telegram-premium",
        "category": "Social & Messengers",
        "icon": "Send",
        "color": "#2AABEE",
        "description": "Загрузка до 4 ГБ, расшифровка голоса, эксклюзивные стикеры, ускоренная загрузка и отключение рекламы.",
        "default_plan_name": "Monthly",
        "popularity_rank": 23,
        "available_plans": ["Monthly"],
        "official_url": "https://telegram.org",
        "guide": "Официально доступна прямая оплата в РФ через @PremiumBot (299 ₽/мес). Через турецкий бот или Fragment можно оплачивать дешевле в TON / лирах.",
        "plans": [
            {
                "id": "monthly", "name": "Monthly", "period": "month", "desc": "Лимиты x2, перевод в реальном времени, эмодзи-статусы.", "us_price": 4.99,
                "prices": {
                    "TR": {"amount": 49.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Через @PremiumBot в Турции", "diff": "easy"},
                    "UA": {"amount": 119, "curr": "UAH", "source": "official", "avail": True, "notes": "Через @PremiumBot в Украине", "diff": "easy"},
                    "IN": {"amount": 179, "curr": "INR", "source": "official", "avail": True, "notes": "Индийский @PremiumBot", "diff": "easy"},
                    "AR": {"amount": 1999, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентина", "diff": "hard"},
                    "KZ": {"amount": 1090, "curr": "KZT", "source": "official", "avail": True, "notes": "Казахстан Kaspi / бот", "diff": "easy"},
                    "NG": {"amount": 1500, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерия", "diff": "medium"},
                    "BR": {"amount": 14.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "PL": {"amount": 19.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "EU": {"amount": 4.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 4.49, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 4.99, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "JP": {"amount": 580, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EG": {"amount": 79.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 139, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "RU": {"amount": 299, "curr": "RUB", "source": "official", "avail": True, "status": "available", "label": "Доступен", "notes": "Официальная прямая оплата картами РФ через бота @PremiumBot без комиссии.", "diff": "easy"}
                }
            }
        ]
    },
    {
        "id": "discord-nitro",
        "name": "Discord Nitro",
        "slug": "discord-nitro",
        "category": "Social & Messengers",
        "icon": "MessageSquare",
        "color": "#5865F2",
        "description": "Стриминг 4K 60fps, кастомные эмодзи по всем серверам, 2 буста сервера и 500 МБ загрузки.",
        "default_plan_name": "Nitro Full",
        "popularity_rank": 24,
        "available_plans": ["Nitro Full"],
        "official_url": "https://discord.com/nitro",
        "guide": "Discord запустил локализованные региональные цены в Турции, Польше и Бразилии. В РФ Discord заблокирован РКН.",
        "plans": [
            {
                "id": "nitro-full", "name": "Nitro Full", "period": "month", "desc": "Все преимущества Nitro, HD-стриминг, 2 буста серверов.", "us_price": 9.99,
                "prices": {
                    "TR": {"amount": 104.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Региональная цена Discord Турция", "diff": "medium"},
                    "PL": {"amount": 19.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Региональная цена Discord Польша", "diff": "easy"},
                    "BR": {"amount": 24.99, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "UA": {"amount": 179, "curr": "UAH", "source": "official", "avail": True, "notes": "Украина", "diff": "easy"},
                    "IN": {"amount": 299, "curr": "INR", "source": "official", "avail": True, "notes": "Индия", "diff": "medium"},
                    "AR": {"amount": 2999, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентина", "diff": "hard"},
                    "NG": {"amount": 2500, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерия", "diff": "medium"},
                    "KZ": {"amount": 4.99, "curr": "USD", "source": "official", "avail": True, "notes": "Казахстан", "diff": "easy"},
                    "EU": {"amount": 9.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 8.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 9.99, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "JP": {"amount": 1050, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EG": {"amount": 119.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 269, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "RU": {"amount": 499, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Заблокирован в РФ", "notes": "Discord заблокирован Роскомнадзором в РФ. Архивный тариф: 499 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20240901000000/https://discord.com/nitro", "date": "2024-09-01"}
                }
            }
        ]
    },
    {
        "id": "icloud-plus",
        "name": "Apple iCloud+ 2TB",
        "slug": "icloud-plus",
        "category": "Cloud & Storage",
        "icon": "Cloud",
        "color": "#3B82F6",
        "description": "2 ТБ для резервных копий и фото на всех устройствах семьи, Частный узел (iCloud Private Relay) и Hide My Email.",
        "default_plan_name": "2TB Monthly",
        "popularity_rank": 25,
        "available_plans": ["2TB Monthly"],
        "official_url": "https://www.apple.com/icloud",
        "guide": "Один из лучших сервисов для прямого использования в РФ: оплачивается со счета мобильного МТС / билайн (749 ₽/мес). Также крайне дешево в Турции.",
        "plans": [
            {
                "id": "2tb-monthly", "name": "2TB Monthly", "period": "month", "desc": "2 ТБ хранилища с возможностью семейного доступа до 5 человек.", "us_price": 9.99,
                "prices": {
                    "TR": {"amount": 249.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Турецкий Apple ID (Gift Cards)", "diff": "easy"},
                    "NG": {"amount": 2900, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерийский Apple ID", "diff": "medium"},
                    "IN": {"amount": 749, "curr": "INR", "source": "official", "avail": True, "notes": "Индийский Apple ID", "diff": "medium"},
                    "AR": {"amount": 5.99, "curr": "USD", "source": "official", "avail": True, "notes": "Аргентина (в USD)", "diff": "medium"},
                    "KZ": {"amount": 5.99, "curr": "USD", "source": "official", "avail": True, "notes": "Казахстан", "diff": "easy"},
                    "UA": {"amount": 6.99, "curr": "USD", "source": "official", "avail": True, "notes": "Украина", "diff": "easy"},
                    "BR": {"amount": 34.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "PL": {"amount": 49.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "EU": {"amount": 9.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 8.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 9.99, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "JP": {"amount": 1300, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EG": {"amount": 179.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 499, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "RU": {"amount": 749, "curr": "RUB", "source": "official", "avail": True, "status": "available", "label": "Доступен", "notes": "Прямая официальная оплата со счета телефона МТС / билайн без комиссий.", "diff": "easy"}
                }
            }
        ]
    },
    {
        "id": "github-copilot",
        "name": "GitHub Copilot",
        "slug": "github-copilot",
        "category": "Dev Tools",
        "icon": "Code2",
        "color": "#24292E",
        "description": "ИИ парное программирование прямо в VS Code, JetBrains и Neovim от GitHub и OpenAI.",
        "default_plan_name": "Individual Monthly",
        "popularity_rank": 29,
        "available_plans": ["Individual Monthly"],
        "official_url": "https://github.com/features/copilot",
        "guide": "GitHub продает Copilot по фиксированной цене $10/мес (или бесплатно для студентов с GitHub Student Developer Pack).",
        "is_global_usd": True,
        "plans": [
            {
                "id": "individual-monthly", "name": "Individual Monthly", "period": "month", "desc": "Безлимитный автокомплит кода, Copilot Chat в IDE.", "us_price": 10.0,
                "prices": {
                    "US": {"amount": 10.00, "curr": "USD", "source": "official", "avail": True, "notes": "Базовая цена", "diff": "easy"},
                    "RU": {"amount": 10.00, "curr": "USD", "source": "usd_flat", "avail": False, "status": "suspended", "label": "Блокировка карт РФ", "notes": "GitHub блокирует прямые оплаты картами РФ.", "diff": "impossible"}
                }
            }
        ]
    },
    {
        "id": "figma-pro",
        "name": "Figma Professional",
        "slug": "figma-pro",
        "category": "Design & Creativity",
        "icon": "Framer",
        "color": "#F24E1E",
        "description": "Безлимитные файлы и проекты, общие библиотеки компонентов, продвинутый Dev Mode.",
        "default_plan_name": "Professional Monthly",
        "popularity_rank": 32,
        "available_plans": ["Professional Monthly"],
        "official_url": "https://www.figma.com/pricing",
        "guide": "Фиксированная цена в USD ($15/мес за редактора). Оплата международными картами.",
        "is_global_usd": True,
        "plans": [
            {
                "id": "pro-monthly", "name": "Professional Monthly", "period": "month", "desc": "Безлимитные проекты, вариативные шрифты, Dev Mode.", "us_price": 15.0,
                "prices": {
                    "US": {"amount": 15.00, "curr": "USD", "source": "official", "avail": True, "notes": "Базовая цена США", "diff": "easy"},
                    "EU": {"amount": 14.00, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "RU": {"amount": 15.00, "curr": "USD", "source": "usd_flat", "avail": False, "status": "suspended", "label": "Ограничено в РФ", "notes": "Figma заморозила корпоративные платные аккаунты из РФ.", "diff": "impossible"}
                }
            }
        ]
    },
    {
        "id": "notion-plus",
        "name": "Notion Plus",
        "slug": "notion-plus",
        "category": "Productivity",
        "icon": "FileCode",
        "color": "#000000",
        "description": "Безлимитные блоки для команд, загрузка файлов без ограничений, история версий 30 дней.",
        "default_plan_name": "Plus Monthly",
        "popularity_rank": 33,
        "available_plans": ["Plus Monthly"],
        "official_url": "https://www.notion.so/pricing",
        "guide": "Notion полностью прекратил обслуживание пользователей из РФ в сентябре 2024 из-за санкций США.",
        "is_global_usd": True,
        "plans": [
            {
                "id": "plus-monthly", "name": "Plus Monthly", "period": "month", "desc": "Безлимитные страницы и блоки, до 100 гостей.", "us_price": 10.0,
                "prices": {
                    "US": {"amount": 10.00, "curr": "USD", "source": "official", "avail": True, "notes": "Базовая цена", "diff": "easy"},
                    "EU": {"amount": 9.50, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "RU": {"amount": 10.00, "curr": "USD", "source": "archive", "avail": False, "status": "suspended", "label": "Ушел из РФ", "notes": "Notion заблокировал воркспейсы из РФ в сентябре 2024.", "diff": "impossible", "url": "https://web.archive.org/web/20240801000000/https://www.notion.so/pricing", "date": "2024-08-01"}
                }
            }
        ]
    },
    {
        "id": "nordvpn",
        "name": "NordVPN Plus",
        "slug": "nordvpn",
        "category": "Security & Privacy",
        "icon": "Shield",
        "color": "#4687FF",
        "description": "Безопасный VPN нового поколения, защита от вредоносных сайтов, трекеров и менеджер паролей NordPass.",
        "default_plan_name": "2-Year Plan (per month)",
        "popularity_rank": 38,
        "available_plans": ["2-Year Plan (per month)"],
        "official_url": "https://nordvpn.com",
        "guide": "Цены указываются при оплате за 2 года вперед с пересчетом за месяц. В РФ протоколы сервиса блокируются ТСПУ.",
        "plans": [
            {
                "id": "2-year", "name": "2-Year Plan (per month)", "period": "month", "desc": "2-летний план: VPN + защита от угроз + менеджер паролей.", "us_price": 3.19,
                "prices": {
                    "US": {"amount": 3.19, "curr": "USD", "source": "official", "avail": True, "notes": "Официальное промо 2-летнего плана", "diff": "easy"},
                    "TR": {"amount": 89.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Турция", "diff": "medium"},
                    "IN": {"amount": 249, "curr": "INR", "source": "official", "avail": True, "notes": "Индия", "diff": "easy"},
                    "AR": {"amount": 2999, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентина", "diff": "hard"},
                    "UA": {"amount": 3.19, "curr": "USD", "source": "official", "avail": True, "notes": "Украина", "diff": "easy"},
                    "KZ": {"amount": 3.19, "curr": "USD", "source": "official", "avail": True, "notes": "Казахстан", "diff": "easy"},
                    "PL": {"amount": 13.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "BR": {"amount": 15.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "EU": {"amount": 3.19, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 2.79, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "JP": {"amount": 490, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "NG": {"amount": 3.19, "curr": "USD", "source": "official", "avail": True, "notes": "Нигерия", "diff": "medium"},
                    "EG": {"amount": 3.19, "curr": "USD", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 179, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "RU": {"amount": 249, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Заблокирован в РФ", "notes": "Протоколы NordVPN блокируются Роскомнадзором в РФ.", "diff": "impossible", "url": "https://web.archive.org/web/20220101000000/https://nordvpn.com", "date": "2022-01-01"}
                }
            }
        ]
    },
    {
        "id": "surfshark-vpn",
        "name": "Surfshark VPN",
        "slug": "surfshark-vpn",
        "category": "Security & Privacy",
        "icon": "ShieldCheck",
        "color": "#188092",
        "description": "Безлимитное количество устройств на одну подписку, блокировка рекламы CleanWeb и высокая скорость.",
        "default_plan_name": "2-Year Plan (per month)",
        "popularity_rank": 39,
        "available_plans": ["2-Year Plan (per month)"],
        "official_url": "https://surfshark.com",
        "guide": "Один из самых выгодных VPN при покупке на 2 года ($2.19/мес). Поддерживает бесконечное число устройств.",
        "plans": [
            {
                "id": "2-year", "name": "2-Year Plan (per month)", "period": "month", "desc": "Безлимитные подключения, CleanWeb, частный DNS.", "us_price": 2.19,
                "prices": {
                    "US": {"amount": 2.19, "curr": "USD", "source": "official", "avail": True, "notes": "Базовое 2-летнее промо", "diff": "easy"},
                    "TR": {"amount": 64.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Турция", "diff": "medium"},
                    "IN": {"amount": 179, "curr": "INR", "source": "official", "avail": True, "notes": "Индия", "diff": "easy"},
                    "AR": {"amount": 2199, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентина", "diff": "hard"},
                    "UA": {"amount": 2.19, "curr": "USD", "source": "official", "avail": True, "notes": "Украина", "diff": "easy"},
                    "KZ": {"amount": 2.19, "curr": "USD", "source": "official", "avail": True, "notes": "Казахстан", "diff": "easy"},
                    "PL": {"amount": 9.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "BR": {"amount": 11.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "EU": {"amount": 2.19, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 1.89, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "JP": {"amount": 330, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "NG": {"amount": 2.19, "curr": "USD", "source": "official", "avail": True, "notes": "Нигерия", "diff": "medium"},
                    "EG": {"amount": 2.19, "curr": "USD", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 129, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "RU": {"amount": 199, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Заблокирован в РФ", "notes": "Surfshark заблокирован Роскомнадзором в РФ.", "diff": "impossible", "url": "https://web.archive.org/web/20220101000000/https://surfshark.com", "date": "2022-01-01"}
                }
            }
        ]
    },
    {
        "id": "jetbrains-all-products",
        "name": "JetBrains All Products",
        "slug": "jetbrains-all-products",
        "category": "Dev Tools",
        "icon": "Terminal",
        "color": "#000000",
        "description": "Пакет лучших IDE: IntelliJ IDEA Ultimate, WebStorm, PyCharm, GoLand, CLion, Rider и др.",
        "default_plan_name": "Individual Monthly",
        "popularity_rank": 40,
        "available_plans": ["Individual Monthly"],
        "official_url": "https://www.jetbrains.com/all",
        "guide": "JetBrains остановил коммерческую деятельность в РФ. Действует накопительная скидка за продление (до 40% на третий год).",
        "is_global_usd": True,
        "plans": [
            {
                "id": "individual-monthly", "name": "Individual Monthly", "period": "month", "desc": "16 десктопных инструментов, профилировщики и плагины.", "us_price": 28.90,
                "prices": {
                    "US": {"amount": 28.90, "curr": "USD", "source": "official", "avail": True, "notes": "Базовая цена первого года", "diff": "easy"},
                    "EU": {"amount": 28.90, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "RU": {"amount": 1490, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Ушел из РФ", "notes": "JetBrains прекратил продажи и поддержку в РФ в марте 2022. Архивный тариф: 1490 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220201000000/https://www.jetbrains.com/ru-ru/", "date": "2022-02-01"}
                }
            }
        ]
    },
    {
        "id": "tradingview",
        "name": "TradingView",
        "slug": "tradingview",
        "category": "Finance",
        "icon": "LineChart",
        "color": "#131722",
        "description": "Профессиональные финансовые графики, технический анализ, скрипты Pine Script и алерты.",
        "default_plan_name": "Essential Monthly",
        "popularity_rank": 41,
        "available_plans": ["Essential Monthly"],
        "official_url": "https://www.tradingview.com/pricing",
        "guide": "В Турции, Аргентине и Индии тариф Essential стоит значительно дешевле стандартных $14.95/мес.",
        "plans": [
            {
                "id": "essential-monthly", "name": "Essential Monthly", "period": "month", "desc": "5 индикаторов на график, 2 графика в окне, без рекламы.", "us_price": 14.95,
                "prices": {
                    "US": {"amount": 14.95, "curr": "USD", "source": "official", "avail": True, "notes": "Базовая цена", "diff": "easy"},
                    "TR": {"amount": 219.00, "curr": "TRY", "source": "official", "avail": True, "notes": "Турция", "diff": "medium"},
                    "IN": {"amount": 999, "curr": "INR", "source": "official", "avail": True, "notes": "Индия", "diff": "easy"},
                    "AR": {"amount": 5999, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентина", "diff": "hard"},
                    "BR": {"amount": 65.00, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "UA": {"amount": 12.95, "curr": "USD", "source": "official", "avail": True, "notes": "Украина", "diff": "easy"},
                    "KZ": {"amount": 14.95, "curr": "USD", "source": "official", "avail": True, "notes": "Казахстан", "diff": "easy"},
                    "PL": {"amount": 59.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "EU": {"amount": 14.95, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 12.95, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "JP": {"amount": 1980, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "NG": {"amount": 6900, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерия", "diff": "medium"},
                    "EG": {"amount": 199.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 599, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "RU": {"amount": 899, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Оплата картами РФ отключена", "notes": "TradingView отключил оплату российскими картами. Архивный тариф: 899 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20220201000000/https://ru.tradingview.com/pricing/", "date": "2022-02-01"}
                }
            }
        ]
    },
    {
        "id": "1password",
        "name": "1Password",
        "slug": "1password",
        "category": "Security & Tools",
        "icon": "KeyRound",
        "color": "#0A85EA",
        "description": "Безопасное хранение паролей, Passkeys, кредитных карт и документов с 256-битным AES шифрованием.",
        "default_plan_name": "Individual Monthly",
        "popularity_rank": 42,
        "available_plans": ["Individual Monthly"],
        "official_url": "https://1password.com",
        "guide": "Глобальный прайс $2.99/мес. 1Password заблокировал пользователей из РФ.",
        "is_global_usd": True,
        "plans": [
            {
                "id": "individual", "name": "Individual Monthly", "period": "month", "desc": "Неограниченное число паролей на всех устройствах.", "us_price": 2.99,
                "prices": {
                    "US": {"amount": 2.99, "curr": "USD", "source": "official", "avail": True, "notes": "Базовая цена", "diff": "easy"},
                    "EU": {"amount": 2.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "RU": {"amount": 2.99, "curr": "USD", "source": "archive", "avail": False, "status": "suspended", "label": "Заблокирован в РФ", "notes": "1Password закрыл доступ для аккаунтов из РФ.", "diff": "impossible", "url": "https://web.archive.org/web/20220301000000/https://1password.com", "date": "2022-03-01"}
                }
            }
        ]
    },
    {
        "id": "tinder-gold",
        "name": "Tinder Gold",
        "slug": "tinder-gold",
        "category": "Lifestyle & Dating",
        "icon": "Flame",
        "color": "#FD3A73",
        "description": "Возможность видеть, кто лайкнул ваш профиль, безлимитные лайки, 5 суперлайков и 1 Boost в месяц.",
        "default_plan_name": "Gold Monthly",
        "popularity_rank": 43,
        "available_plans": ["Gold Monthly"],
        "official_url": "https://tinder.com",
        "guide": "В Турции, Аргентине и Индии подписка стоит в 2–3 раза дешевле. Match Group отключила работу Tinder в РФ в июне 2023.",
        "plans": [
            {
                "id": "gold-monthly", "name": "Gold Monthly", "period": "month", "desc": "Узнайте, кто вас лайкнул, Passport в любой город.", "us_price": 24.99,
                "prices": {
                    "TR": {"amount": 149.99, "curr": "TRY", "source": "official", "avail": True, "notes": "Турция", "diff": "medium"},
                    "AR": {"amount": 2999, "curr": "ARS", "source": "official", "avail": True, "notes": "Аргентина", "diff": "hard"},
                    "IN": {"amount": 499, "curr": "INR", "source": "official", "avail": True, "notes": "Индия", "diff": "easy"},
                    "NG": {"amount": 3200, "curr": "NGN", "source": "official", "avail": True, "notes": "Нигерия", "diff": "medium"},
                    "BR": {"amount": 39.90, "curr": "BRL", "source": "official", "avail": True, "notes": "Бразилия", "diff": "medium"},
                    "UA": {"amount": 7.99, "curr": "USD", "source": "official", "avail": True, "notes": "Украина", "diff": "easy"},
                    "KZ": {"amount": 8.99, "curr": "USD", "source": "official", "avail": True, "notes": "Казахстан", "diff": "easy"},
                    "PL": {"amount": 49.99, "curr": "PLN", "source": "official", "avail": True, "notes": "Польша", "diff": "easy"},
                    "EU": {"amount": 19.99, "curr": "EUR", "source": "official", "avail": True, "notes": "Еврозона", "diff": "easy"},
                    "GB": {"amount": 14.99, "curr": "GBP", "source": "official", "avail": True, "notes": "Великобритания", "diff": "easy"},
                    "US": {"amount": 24.99, "curr": "USD", "source": "official", "avail": True, "notes": "США", "diff": "easy"},
                    "JP": {"amount": 2800, "curr": "JPY", "source": "official", "avail": True, "notes": "Япония", "diff": "medium"},
                    "EG": {"amount": 199.99, "curr": "EGP", "source": "official", "avail": True, "notes": "Египет", "diff": "medium"},
                    "PH": {"amount": 399, "curr": "PHP", "source": "official", "avail": True, "notes": "Филиппины", "diff": "easy"},
                    "RU": {"amount": 499, "curr": "RUB", "source": "archive", "avail": False, "status": "suspended", "label": "Ушел из РФ", "notes": "Match Group отключила Tinder в РФ в июне 2023. Архивный тариф: 499 ₽.", "diff": "impossible", "url": "https://web.archive.org/web/20230501000000/https://tinder.com", "date": "2023-05-01"}
                }
            }
        ]
    }
]

print("Productivity Services definitions loaded")
