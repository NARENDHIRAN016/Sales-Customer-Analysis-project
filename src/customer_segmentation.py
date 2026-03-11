import pandas as pd

def perform_rfm_analysis(df):
    rfm = df.groupby("Customer_ID").agg({
        "Order_Date": lambda x: (df["Order_Date"].max() - x.max()).days,
        "Order_ID": "count",
        "Sales": "sum"
    })
    rfm.columns = ["Recency", "Frequency", "Monetary"]
    return rfm