def calculate_kpis(df):
    total_revenue = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    aov = total_revenue / df["Order_ID"].nunique()
    profit_margin = (total_profit / total_revenue) * 100
    return total_revenue, total_profit, aov, profit_margin

def plot_category_sales(df):
    category_sales = df.groupby("Product_Category")["Sales"].sum()
    category_sales.plot(kind="bar")
    plt.title("Sales by Product Category")
    plt.show()