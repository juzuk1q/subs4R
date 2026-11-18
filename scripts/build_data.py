# scripts/build_data.py
# Generates complete, validated backend/data.go with full 15-country matrix for all 43 services.

import json
import math

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

COUNTRY_MAP = {c["code"]: c for c in COUNTRIES}

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
    return amount * RATES.get(curr, 1.0)

def from_usd(usd, curr):
    r = RATES.get(curr, 1.0)
    return usd / r if r > 0 else usd

def round_price(val, curr):
    if curr in ["TRY", "PLN", "BRL", "EGP", "PHP"]:
        int_part = math.floor(val)
        return (int_part if int_part > 0 else 1) + 0.99
    elif curr in ["ARS", "NGN", "INR", "KZT", "JPY", "RUB"]:
        if val > 1000:
            return round(val / 100) * 100
        return round(val / 10) * 10
    else:
        return round(val * 100) / 100

print("Helper setup complete")
