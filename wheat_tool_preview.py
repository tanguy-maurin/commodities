# Wheat_Tool — Chapter 1 Preview
# Hardcoded data. Scraping comes in Chapter 5.

print("=" * 40)
print("   WHEAT TOOL — MARKET SNAPSHOT")
print("=" * 40)

# --- Data (will be fetched dynamically later) ---
assets = [
    ("Brent Crude",  "Oil",  82.47, 80.10, "USD"),
    ("EUR/USD",      "FX",    1.085,  1.079, "USD"),
    ("Gold",         "Metal", 2310.0, 2285.5, "USD"),
]

# --- Display ---
for name, category, price, prev, currency in assets:
    change = price - prev
    pct = (change / prev) * 100
    arrow = "▲" if change > 0 else "▼"
    print(f"{arrow} {name:<14} [{category}]  {price:.2f} {currency}  ({pct:+.1f}%)")

print("=" * 40)
print("Data as of: 2026-03-16  [hardcoded]")