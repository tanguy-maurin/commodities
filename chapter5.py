import pandas as pd
import requests

"""
response = requests.get("https://open.er-api.com/v6/latest/USD")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")






rates = [{"currency":k, "rate":v} for k, v in data["rates"].items()]
df2 = pd.DataFrame(rates)
"""

def get_rate(currency):
    response = requests.get("https://open.er-api.com/v6/latest/USD")
    if response.status_code == 200 :
        data = response.json()
        return data["rates"][currency]
    else:
        print(f"Error: Status code {response.status_code}")


def fetch_fx_rates(base_currency) :
    response = requests.get(f"https://open.er-api.com/v6/latest/{base_currency}")
    if response.status_code == 200 :
        data = response.json()
        records = [{"currency": k, "rate": v} for k, v in data["rates"].items()]
        df = pd.DataFrame(records)
        return(df)
    else:
        print(f"Request failed with status code: {response.status_code}")
        return(None)

print(fetch_fx_rates("USD"))