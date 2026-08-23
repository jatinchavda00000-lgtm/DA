import pandas as pd
import matplotlib.pyplot as plt

# 1. Load sales dataset
df = pd.read_csv("data/sample_sales_data.csv", parse_dates=["date"])

# Verify first 5 rows
print("First 5 rows:")
print(df.head())

# 2. Total sales by category + bar chart
category_sales = df.groupby("category")["sales_amount"].sum().sort_values(ascending=False)

plt.figure(figsize=(9, 5))
bars = plt.bar(category_sales.index, category_sales.values)
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales Amount")

# 5. Add exact value annotations
for bar, value in zip(bars, category_sales.values):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{value:,.0f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("charts/category_sales_kpi.png", dpi=200, bbox_inches="tight")
plt.show()

# 3. Monthly sales trend
monthly_sales = (
    df.assign(month=df["date"].dt.to_period("M"))
      .groupby("month")["sales_amount"]
      .sum()
)

plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend - 2025")
plt.xlabel("Month")
plt.ylabel("Total Sales Amount")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("charts/monthly_sales_trend.png", dpi=200, bbox_inches="tight")
plt.show()

# 4. Distribution of order amounts
plt.figure(figsize=(9, 5))
plt.hist(df["sales_amount"], bins=10, edgecolor="black")
plt.title("Distribution of Order Amounts")
plt.xlabel("Order Amount / Sales Value")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("charts/order_amount_distribution.png", dpi=200, bbox_inches="tight")
plt.show()
