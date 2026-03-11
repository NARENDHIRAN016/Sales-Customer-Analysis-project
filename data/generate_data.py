import pandas as pd
import numpy as np

np.random.seed(42)
rows = 1500

data = {
    "Order_ID": np.arange(1001, 1001 + rows),
    "Order_Date": pd.date_range("2022-01-01", periods=rows, freq="D"),
    "Customer_ID": np.random.randint(200, 500, rows),
    "Customer_Segment": np.random.choice(["Consumer", "Corporate", "Home Office"], rows),
    "Gender": np.random.choice(["Male", "Female"], rows),
    "Age": np.random.randint(18, 65, rows),
    "Region": np.random.choice(["North", "South", "East", "West"], rows),
    "Product_Category": np.random.choice(["Electronics", "Furniture", "Clothing"], rows),
    "Product_Name": np.random.choice(["Product A", "Product B", "Product C"], rows),
    "Quantity": np.random.randint(1, 6, rows),
    "Unit_Price": np.random.randint(200, 5000, rows),
    "Discount": np.round(np.random.uniform(0, 0.3, rows), 2),
    "Payment_Method": np.random.choice(["UPI", "Card", "Cash", "Net Banking"], rows)
}

df = pd.DataFrame(data)
df["Sales"] = df["Quantity"] * df["Unit_Price"] * (1 - df["Discount"])
df["Profit"] = df["Sales"] * np.random.uniform(0.05, 0.25, rows)

df.to_csv("raw_sales_data.csv", index=False)