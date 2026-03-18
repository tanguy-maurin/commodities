def get_signal(name, price):
    """Return a string composed of the commodity name and a buy/hold signal."""
    if price < 80:
            signal = "BUY"
    else:
            signal = "HOLD"
    return name + ": " + signal

def get_commodity_snapshot(name, price, currency="USD", unit="barrel"):
    """Returns a commodity snapshot dictionnary witha buy/hold signal"""
    if price < 80:
        signal = "BUY"
    else:
        signal = "HOLD"
    return {
        "name" : name,
        "price" : price,
        "currency" : currency,
        "unit" : unit,
        "signal" : signal
    }

def summarize_portfolio(commodities):
    """returns a dictionnary presenting data about a list of commodities"""
    total_value = 0
    for c in commodities:
        total_value += c["price"]
    return {
        "count" : len(commodities),
        "total_value" : total_value,
        "average_price" : total_value/len(commodities)
    }

commodities_list = [
    get_commodity_snapshot("Oil", 83.7),
    get_commodity_snapshot("Gold", 126.0, "USD" , "ounce"),
    get_commodity_snapshot("Wheat", 45.9, "EUR", "bushel")
]

print(summarize_portfolio(commodities_list))