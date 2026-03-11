import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_distribution(df):
    sns.histplot(df["Sales"], bins=30)
    plt.title("Sales Distribution")
    plt.xlabel("Sales Amount")
    plt.ylabel("Frequency")
    plt.show()

def plot_discount_vs_profit(df):
    sns.scatterplot(x="Discount", y="Profit", data=df)
    plt.title("Discount vs Profit")
    plt.show()