import pandas as pd

df = pd.read_csv("task4_delivery_performance.csv")

# Convert columns to numeric for calculations.
df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")
df["DeliveryTime"] = pd.to_numeric(df["DeliveryTime"], errors="coerce")

# Aggregate by cuisine.
summary = (
    df.groupby("Cuisine", dropna=False)
      .agg(
          Total_Revenue=("Revenue", "sum"),
          Average_DeliveryTime=("DeliveryTime", "mean"),
          Order_Count=("OrderID", "count"),
      )
      .reset_index()
)

# Negative delivery times are left in the data.
# This can bias the mean downward and is a data-quality gap, not a real operational value.
df["PerformanceFlag"] = df["DeliveryTime"].apply(
    lambda x: "Delayed" if x > 60 else "On Time"
)

corr = df[["Revenue", "DeliveryTime", "Rating"]].corr()

print("=== Cuisine Summary ===")
print(summary.to_string(index=False))
print("\n=== Correlation Matrix ===")
print(corr.round(3).to_string())

with pd.ExcelWriter("food_delivery_summary.xlsx", engine="openpyxl") as writer:
    summary.to_excel(writer, sheet_name="Cuisine Summary", index=False)
    df.to_excel(writer, sheet_name="Enriched Data", index=False)
