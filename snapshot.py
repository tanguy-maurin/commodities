commodity = "Brent Crude"
price = 82.47
currency = "USD"
date = "2026-03-16"
previous_close = 80.10

change = price - previous_close
pct_change = (change / previous_close) * 100

print(f"=== COMMODITY SNAPSHOT ===")
print(f"Commodity : {commodity}")
print(f"Date      : {date}")
print(f"Price     : {price} {currency}")
print(f"Prev Close: {previous_close} {currency}")
print(f"Change    : {change:+.2f} {currency} ({pct_change:+.1f}%)")