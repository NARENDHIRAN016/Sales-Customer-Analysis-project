import pandas as pd

def clean_data(df):
    df = df.drop_duplicates()
    df["Order_Date"] = pd.to_datetime(df["Order_Date"])

    df["Year"] = df["Order_Date"].dt.year
    df["Month"] = df["Order_Date"].dt.month
    df["Quarter"] = df["Order_Date"].dt.to_period("Q")

    # Outlier capping
    df["Sales"] = df["Sales"].clip(upper=df["Sales"].quantile(0.99))
    df["Profit"] = df["Profit"].clip(upper=df["Profit"].quantile(0.99))

    return df