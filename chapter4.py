import pandas as pd

df = pd.read_csv("sample_commodities.csv")
df = df[df["price"]>50]
df["signal"] = df["price"] < 80


def load_commodity_data(filepath, price_col):
    """
    Reads a commodity CSV, renames the price column, drops missing values,
    and adds a buy signal where price is strictly less than 80.

    Args:
        filepath (str): Path to the CSV file.
        price_col (str): Name of the column to use as price.

    Returns:
        pd.DataFrame: Cleaned DataFrame with a 'signal' column.
    """
    df_commo = pd.read_csv(filepath)
    df_commo = df_commo.dropna()
    df_commo = df_commo.rename(columns={price_col:"price"})
    df_commo["signal"] = df_commo["price"]<80
    return df_commo



def get_buy_signals(df):
    df1 = df[df["signal"]==True]
    df1 = df1[["commodity", "price"]]
    return df1

print(get_buy_signals(load_commodity_data("sample_commodities.csv", "price")))