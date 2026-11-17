# 🎮 subs4R — Global Subscription Price Matrix

Агрегатор и сравнительная матрица региональных цен на цифровые подписки и сервисы (в стиле SteamDB): **YouTube, Spotify, Netflix, ChatGPT, Claude, Xbox Game Pass, PlayStation Plus, Telegram Premium, Steam** и 35+ других сервисов по странам мира (Турция 🇹🇷, Нигерия 🇳🇬, Аргентина 🇦🇷, Казахстан 🇰🇿, Индия 🇮🇳, Польша 🇵🇱, Украина 🇺🇦, США 🇺🇸).

---

## 🛠 Стек технологий

* **Backend:** Go (Golang 1.24) — быстрый легковесный REST API на стандартной библиотеке `net/http` со слоем провайдеров (`MSStoreProvider`, `SteamProvider`), защитой от аномалий (>30%), типизированными статусами и автоматическим обновлением курсов 160+ валют с `open.er-api.com`.
* **Frontend:** React 19 + TypeScript + Vite + Tailwind CSS + Lucide Icons + Oxlint.
* **Архитектура UI:** Чистое разделение по слоям ответственности:
  - `src/views/` — экраны аналитики (`MatrixView`, `CalculatorView`)
  - `src/components/layout/` — навигация и шапка (`Navbar`)
  - `src/components/modals/` — модальные окна (`ServiceDetailModal`, `SuggestModal`)
  - `src/components/ui/` — переиспользуемые атомы (`Flag`, `ServiceLogo`, `Sparkline`)
* **Контейнеризация:** Multi-stage `Dockerfile` (Alpine) и кроссплатформенный `Makefile`.

---

## 🚀 Быстрый старт

### Способ 1: Через Docker (рекомендуется для продакшна)

```bash
# Сборка multi-stage контейнера
docker build -t subs4r .

# Запуск на порту 8080
docker run --rm -p 8080:8080 subs4r
```
Приложение сразу доступно по адресу **http://localhost:8080**.

---

### Способ 2: Через Makefile

```bash
# Сборка фронтенда и бэкенда
make build

# Запуск бэкенда
./subs4r-server
```

Для режима разработки:
```bash
# Терминал 1 (Бэкенд Go API :8080):
make dev-back

# Терминал 2 (Фронтенд Vite :5173):
make dev-front
```

---

### Способ 3: Для Windows

Скрипты вынесены в директорию `scripts/`:
* `scripts/start.bat` — компиляция и запуск сервера в один клик.
* `scripts/dev.bat` — параллельный запуск Vite и Go API.

---

## 📁 Структура проекта

```text
subs4R/
├── backend/
│   ├── data.go        # База сервисов, планов и тарифов по странам
│   ├── go.mod         # Модуль Go (subs4r)
│   ├── main.go        # HTTP роуты, middleware, раздача статики
│   ├── models.go      # Типизированные структуры, ошибки (ErrNotAvailable, ErrGlobalUSD)
│   └── providers.go   # Слой провайдеров (MS Store API, Steam API, open.er-api.com)
├── public/            # Фавиконы и векторные ассеты
├── src/
│   ├── components/
│   │   ├── layout/    # Navbar.tsx
│   │   ├── modals/    # ServiceDetailModal.tsx, SuggestModal.tsx
│   │   └── ui/        # Flag.tsx, ServiceLogo.tsx, Sparkline.tsx
│   ├── views/         # MatrixView.tsx, CalculatorView.tsx
│   ├── App.tsx        # Главный экран и таблица сервисов
│   ├── index.css      # Стили SteamDB темы
│   ├── main.tsx       # Точка входа React
│   └── types.ts       # Интерфейсы TypeScript
├── Dockerfile         # Multi-stage production build (Node -> Go -> Alpine)
├── Makefile           # Кроссплатформенный запуск и сборка
└── package.json       # Зависимости и скрипты фронтенда
```

---

## 🌟 Возможности

1. **Матрица цен (Country Matrix):** Сравнительная сетка «Сервисы ✕ Страны» с автоматической подсветкой минимальной цены в строке.
2. **Информативные статусы:** Вместо прочерков выводятся статусы `🚫 Не запущен` (нет регионального стора) и `🌐 Global $` (нет региональной валюты, списание в USD).
3. **Защита от аномалий:** Провайдеры отслеживают скачки цен >30% и не применяют их моментально, предотвращая порчу базы промо-акциями.
4. **Спарклайны истории цен:** SVG-график изменения стоимости за последние месяцы.
5. **Калькулятор экономии:** Подсчет годовой выгоды при переходе на региональные подписки.
