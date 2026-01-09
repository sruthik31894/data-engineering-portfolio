import pandas as pd

def extract():
    return pd.read_csv("../sample_data/sales_data.csv")

def transform(df):
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["revenue"] = df["quantity"] * df["price"]
    return df

def load(df):
    df.to_csv("../sample_data/processed_sales_data.csv", index=False)

if __name__ == "__main__":
    df = extract()
    df = transform(df)
    load(df)
