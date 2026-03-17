
commodities = [
    {"name": "WTI", "price":87.3, "signal":None},
    {"name" : "Brent", "price":103.6, "signal":None}
]

for c_i in commodities :
    if c_i["price"] > 100 :
        c_i["signal"] = "SELL"
    elif c_i["price"] < 50 :
        c_i["signal"] = "BUY"
    else :
        c_i["signal"] = "HOLD"
    print(f"{c_i["name"]} : {c_i["signal"]}")

data = [
    {"name": "Gold", "price": 1923.4},
    {"name": "Silver", "price": 24.3},
    {"name": "Copper", "price": 8.7}
]

result = []

for item in data:
    if item["price"] < 100:
        result.append(item["name"])

print(result)