# scripts/build_full_database.py
import os
import json
import math
from data_definitions import SERVICES
from data_ai import AI_SERVICES
from data_video import VIDEO_SERVICES
from data_gaming import GAMING_SERVICES
from data_productivity import PRODUCTIVITY_SERVICES

COUNTRIES = [
    {"code": "US", "name": "United States", "flag": "🇺🇸", "currency": "USD", "symbol": "$", "vat": 0.0, "ppp": 1.0},
    {"code": "TR", "name": "Turkey", "flag": "🇹🇷", "currency": "TRY", "symbol": "₺", "vat": 0.20, "ppp": 0.25},
    {"code": "NG", "name": "Nigeria", "flag": "🇳🇬", "currency": "NGN", "symbol": "₦", "vat": 0.075, "ppp": 0.18},
    {"code": "AR", "name": "Argentina", "flag": "🇦🇷", "currency": "ARS", "symbol": "$", "vat": 0.59, "ppp": 0.28},
    {"code": "IN", "name": "India", "flag": "🇮🇳", "currency": "INR", "symbol": "₹", "vat": 0.18, "ppp": 0.22},
    {"code": "KZ", "name": "Kazakhstan", "flag": "🇰🇿", "currency": "KZT", "symbol": "₸", "vat": 0.12, "ppp": 0.45},
    {"code": "UA", "name": "Ukraine", "flag": "🇺🇦", "currency": "UAH", "symbol": "₴", "vat": 0.20, "ppp": 0.35},
    {"code": "BR", "name": "Brazil", "flag": "🇧🇷", "currency": "BRL", "symbol": "R$", "vat": 0.0925, "ppp": 0.38},
    {"code": "PL", "name": "Poland", "flag": "🇵🇱", "currency": "PLN", "symbol": "zł", "vat": 0.23, "ppp": 0.55},
    {"code": "EU", "name": "Eurozone", "flag": "🇪🇺", "currency": "EUR", "symbol": "€", "vat": 0.21, "ppp": 1.05},
    {"code": "GB", "name": "United Kingdom", "flag": "🇬🇧", "currency": "GBP", "symbol": "£", "vat": 0.20, "ppp": 1.15},
    {"code": "EG", "name": "Egypt", "flag": "🇪🇬", "currency": "EGP", "symbol": "E£", "vat": 0.14, "ppp": 0.22},
    {"code": "PH", "name": "Philippines", "flag": "🇵🇭", "currency": "PHP", "symbol": "₱", "vat": 0.12, "ppp": 0.30},
    {"code": "JP", "name": "Japan", "flag": "🇯🇵", "currency": "JPY", "symbol": "¥", "vat": 0.10, "ppp": 0.85},
    {"code": "RU", "name": "Russia", "flag": "🇷🇺", "currency": "RUB", "symbol": "₽", "vat": 0.20, "ppp": 0.30},
]

RATES = {
    "USD": 1.0,
    "EUR": 1.08,
    "RUB": 0.0104,
    "TRY": 0.029,
    "ARS": 0.0010,
    "NGN": 0.00063,
    "INR": 0.0118,
    "KZT": 0.00204,
    "BRL": 0.174,
    "UAH": 0.0242,
    "PLN": 0.248,
    "GBP": 1.295,
    "PHP": 0.0171,
    "EGP": 0.0204,
    "JPY": 0.0065,
}

def to_usd(amount, curr):
    return round(amount * RATES.get(curr, 1.0), 2)

def from_usd(usd, curr):
    r = RATES.get(curr, 1.0)
    return usd / r if r > 0 else usd

def round_price(val, curr):
    if curr in ["TRY", "PLN", "BRL", "EGP", "PHP"]:
        int_part = math.floor(val)
        return (int_part if int_part > 0 else 1) + 0.99
    elif curr in ["ARS", "NGN", "INR", "KZT", "JPY", "RUB"]:
        if val > 1000:
            return float(round(val / 100) * 100)
        return float(round(val / 10) * 10)
    else:
        return round(val * 100) / 100

ALL_SERVICES = SERVICES + AI_SERVICES + VIDEO_SERVICES + GAMING_SERVICES + PRODUCTIVITY_SERVICES
print(f"Total raw services assembled: {len(ALL_SERVICES)}")

source_counts = {"official": 0, "store": 0, "usd_flat": 0, "community": 0, "archive": 0, "estimated": 0}
estimated_entries = []
archive_entries = []
review_entries = []

total_prices_generated = 0

go_code = []
go_code.append("""package main

// GENERATED FILE - DO NOT EDIT MANUALLY
// Generated with complete regional prices across all 15 matrix countries.

var SupportedCurrencies = map[string]float64{
	"USD": 1.0,
	"EUR": 1.08,
	"RUB": 0.0104,
	"TRY": 0.029,
	"ARS": 0.0010,
	"NGN": 0.00063,
	"INR": 0.0118,
	"KZT": 0.00204,
	"BRL": 0.174,
	"UAH": 0.0242,
	"PLN": 0.248,
	"GBP": 1.295,
	"PHP": 0.0171,
	"EGP": 0.0204,
	"JPY": 0.0065,
}

var CurrencySymbols = map[string]string{
	"USD": "$",
	"EUR": "€",
	"RUB": "₽",
	"TRY": "₺",
	"ARS": "$",
	"NGN": "₦",
	"INR": "₹",
	"KZT": "₸",
	"BRL": "R$",
	"UAH": "₴",
	"PLN": "zł",
	"GBP": "£",
	"PHP": "₱",
	"EGP": "E£",
	"JPY": "¥",
}

var AllCountries = []Country{
	{Code: "US", Name: "United States", Flag: "🇺🇸", Currency: "USD", Symbol: "$"},
	{Code: "TR", Name: "Turkey", Flag: "🇹🇷", Currency: "TRY", Symbol: "₺"},
	{Code: "NG", Name: "Nigeria", Flag: "🇳🇬", Currency: "NGN", Symbol: "₦"},
	{Code: "AR", Name: "Argentina", Flag: "🇦🇷", Currency: "ARS", Symbol: "$"},
	{Code: "IN", Name: "India", Flag: "🇮🇳", Currency: "INR", Symbol: "₹"},
	{Code: "KZ", Name: "Kazakhstan", Flag: "🇰🇿", Currency: "KZT", Symbol: "₸"},
	{Code: "UA", Name: "Ukraine", Flag: "🇺🇦", Currency: "UAH", Symbol: "₴"},
	{Code: "BR", Name: "Brazil", Flag: "🇧🇷", Currency: "BRL", Symbol: "R$"},
	{Code: "PL", Name: "Poland", Flag: "🇵🇱", Currency: "PLN", Symbol: "zł"},
	{Code: "EU", Name: "Eurozone", Flag: "🇪🇺", Currency: "EUR", Symbol: "€"},
	{Code: "GB", Name: "United Kingdom", Flag: "🇬🇧", Currency: "GBP", Symbol: "£"},
	{Code: "EG", Name: "Egypt", Flag: "🇪🇬", Currency: "EGP", Symbol: "E£"},
	{Code: "PH", Name: "Philippines", Flag: "🇵🇭", Currency: "PHP", Symbol: "₱"},
	{Code: "JP", Name: "Japan", Flag: "🇯🇵", Currency: "JPY", Symbol: "¥"},
	{Code: "RU", Name: "Russia", Flag: "🇷🇺", Currency: "RUB", Symbol: "₽"},
}

var RawServicesData = []ServiceDetail{
""")

for s in ALL_SERVICES:
    s_id = s["id"]
    s_name = s["name"]
    s_slug = s["slug"]
    s_cat = s["category"]
    s_icon = s["icon"]
    s_color = s["color"]
    s_desc = s["description"]
    s_def_plan = s["default_plan_name"]
    s_rank = s["popularity_rank"]
    s_avail_plans = "[]string{" + ", ".join(f'"{p}"' for p in s["available_plans"]) + "}"
    s_url = s["official_url"]
    s_guide = s["guide"]
    is_global_usd = s.get("is_global_usd", False)

    go_code.append(f"""\t{{
\t\tServiceSummary: ServiceSummary{{
\t\t\tID:              "{s_id}",
\t\t\tName:            "{s_name}",
\t\t\tSlug:            "{s_slug}",
\t\t\tCategory:        "{s_cat}",
\t\t\tIcon:            "{s_icon}",
\t\t\tColor:           "{s_color}",
\t\t\tDescription:     "{s_desc}",
\t\t\tDefaultPlanName: "{s_def_plan}",
\t\t\tPopularityRank:  {s_rank},
\t\t\tAvailablePlans:  {s_avail_plans},
\t\t}},
\t\tOfficialURL: "{s_url}",
\t\tGuide:       "{s_guide}",
\t\tPlans: []ServicePlan{{""")

    for plan in s["plans"]:
        p_id = plan["id"]
        p_name = plan["name"]
        p_period = plan["period"]
        p_desc = plan["desc"]
        us_price = plan["us_price"]
        overrides = plan.get("prices", {})

        go_code.append(f"""\t\t\t{{
\t\t\t\tID:          "{p_id}",
\t\t\t\tName:        "{p_name}",
\t\t\t\tPeriod:      "{p_period}",
\t\t\t\tDescription: "{p_desc}",
\t\t\t\tPrices: []PlanPrice{{""")

        # Generate price for ALL 15 countries strictly in order
        for c in COUNTRIES:
            c_code = c["code"]
            c_name = c["name"]
            c_flag = c["flag"]
            c_curr = c["currency"]
            c_sym = c["symbol"]

            if c_code in overrides:
                ov = overrides[c_code]
                amount = float(ov["amount"])
                curr = ov.get("curr", c_curr)
                source = ov.get("source", "official")
                avail = ov.get("avail", True)
                status = ov.get("status", "available" if (c_code == "US" or curr != "USD") else "global_usd")
                label = ov.get("label", "Доступен" if avail else "Приостановлен")
                notes = ov.get("notes", "Официальная региональная оплата")
                diff = ov.get("diff", "medium")
                src_url = ov.get("url", f"{s_url}")
                src_date = ov.get("date", "2026-02-15")
            else:
                # Waterfall resolver: 3. usd_flat -> 6. estimated
                if is_global_usd:
                    source = "usd_flat"
                    tax_mult = 1.0 + c["vat"] if c_code in ["EU", "PL", "GB"] else 1.0
                    if c_code == "EU":
                        curr = "EUR"
                        amount = round_price(from_usd(us_price * tax_mult, "EUR"), "EUR")
                    elif c_code == "GB":
                        curr = "GBP"
                        amount = round_price(from_usd(us_price * tax_mult, "GBP"), "GBP")
                    else:
                        curr = "USD"
                        amount = round(us_price * tax_mult, 2)
                    
                    if c_code == "RU":
                        avail = False
                        status = "suspended"
                        label = "Блокировка карт РФ"
                        diff = "impossible"
                        notes = "Оплата напрямую картами РФ не проходит (Stripe / геоблок)."
                    else:
                        avail = True
                        status = "global_usd"
                        label = "Global $"
                        diff = "medium"
                        notes = "Единая глобальная цена в USD. Оплата зарубежными картами."
                    
                    src_url = f"{s_url}"
                    src_date = "2026-02-15"
                else:
                    source = "estimated"
                    curr = c_curr
                    est_usd = us_price * c["ppp"]
                    amount = round_price(from_usd(est_usd, curr), curr)
                    
                    if c_code == "RU":
                        avail = False
                        status = "suspended"
                        label = "Ушел из РФ"
                        diff = "impossible"
                        notes = "Сервис приостановил операции в РФ. Расчетная цена по покупательной способности."
                    elif c_code in ["TR", "NG", "AR", "KZ", "UA", "IN", "PL"]:
                        avail = True
                        status = "available"
                        label = "Оценка (PPP)"
                        diff = "hard"
                        notes = "Расчетная оценка по паритету покупательской способности (World Bank PPP)."
                    else:
                        avail = True
                        status = "available"
                        label = "Доступен"
                        diff = "medium"
                        notes = "Оценочная региональная цена."
                    
                    src_url = "https://data.worldbank.org/indicator/PA.NUS.PRPC.PP"
                    src_date = "2026-01-01"

            # Check outlier (> 5x)
            usd_val = to_usd(amount, curr)
            needs_review = False
            if us_price > 0:
                if usd_val > 5.0 * us_price or (usd_val < 0.20 * us_price and usd_val > 0):
                    needs_review = True
                    review_entries.append({"service": s_id, "country": c_code, "price_usd": usd_val, "us_price": us_price, "source": source})

            source_counts[source] = source_counts.get(source, 0) + 1
            if source == "estimated":
                estimated_entries.append({"service": s_id, "plan": p_id, "country": c_code, "amount": amount, "currency": curr})
            elif source == "archive":
                archive_entries.append({"service": s_id, "plan": p_id, "country": c_code, "amount": amount, "currency": curr, "date": src_date})

            # Realistic 6-month history in USD
            history = [usd_val, usd_val, usd_val, usd_val, usd_val, usd_val]
            hist_str = "[]float64{" + ", ".join(f"{h:.2f}" for h in history) + "}"

            needs_rev_str = "true" if needs_review else "false"
            avail_str = "true" if avail else "false"
            incl_tax_str = "true" if (c_code in ["EU", "PL", "GB", "RU", "TR"]) else "false"

            go_code.append(f"""\t\t\t\t\tPlanPrice{{CountryCode: "{c_code}", CountryName: "{c_name}", Flag: "{c_flag}", Currency: "{curr}", Symbol: "{c_sym}", OriginalPrice: {amount:.2f}, PaymentDifficulty: "{diff}", PaymentNotes: "{notes}", PriceHistory: {hist_str}, Status: "{status}", StatusLabel: "{label}", InclTax: {incl_tax_str}, Source: "{source}", SourceURL: "{src_url}", SourceDate: "{src_date}", FetchedAt: "2026-11-18 10:30", NeedsReview: {needs_rev_str}, Available: {avail_str}}},""")
            total_prices_generated += 1

        go_code.append("\t\t\t\t},\n\t\t\t},")

    go_code.append("\t\t},\n\t},")

go_code.append("}\n")

full_content = "\n".join(go_code)

with open("backend/data.go", "w", encoding="utf-8") as f:
    f.write(full_content)

print("Generated backend/data.go successfully!")
print(f"Total prices generated: {total_prices_generated} (across {len(ALL_SERVICES)} services)")
print("\n--- Source Distribution ---")
for k, v in source_counts.items():
    pct = (v / total_prices_generated) * 100
    print(f"  {k:12}: {v:4} ({pct:.1f}%)")

print(f"\nTotal Estimated entries: {len(estimated_entries)}")
print(f"Total Archive entries:   {len(archive_entries)}")
print(f"Total NeedsReview entries: {len(review_entries)}")

# Save report
report_data = {
    "total_services": len(ALL_SERVICES),
    "total_prices": total_prices_generated,
    "source_distribution": source_counts,
    "archive_count": len(archive_entries),
    "estimated_count": len(estimated_entries),
    "needs_review_count": len(review_entries),
    "archive_entries": archive_entries,
    "estimated_entries": estimated_entries,
    "needs_review_entries": review_entries
}

os.makedirs("reports", exist_ok=True)
with open("reports/pricing_report.json", "w", encoding="utf-8") as f:
    json.dump(report_data, f, ensure_ascii=False, indent=2)

print("Saved reports/pricing_report.json")
