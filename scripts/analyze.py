import re

with open('backend/data.go', 'r', encoding='utf-8') as f:
    text = f.read()

matrix_countries = ["US", "TR", "NG", "AR", "IN", "KZ", "UA", "BR", "PL", "EU", "GB", "EG", "PH", "JP", "RU"]

# Let's count how many total prices exist currently
price_blocks = re.findall(r'CountryCode:\s*"([^"]+)"', text)
print(f"Total price entries in data.go: {len(price_blocks)}")
