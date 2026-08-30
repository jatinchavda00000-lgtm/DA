import pandas as pd
from pathlib import Path

INPUT_CSV = "task4_delivery_performance.csv"
OUTPUT_XLSX = "food_delivery_summary.xlsx"

df = pd.read_csv(INPUT_CSV)

# Coerce numeric fields so blank Revenue values become NaN rather than raising an error.
df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce")
df["DeliveryTime"] = pd.to_numeric(df["DeliveryTime"], errors="coerce")
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

# Blank rows are excluded from analysis; they are not silently converted into zero-value orders.
df = df.dropna(how="all").copy()

# Negative delivery time is a data-entry/tracking error, so it is flagged as invalid and set to NaN.
invalid_dt = df["DeliveryTime"] < 0
df.loc[invalid_dt, "DeliveryTime"] = pd.NA

# A NaN DeliveryTime cannot be called "Delayed"; use "Invalid / Missing" to keep the issue visible.
df["PerformanceFlag"] = "On Time"
df.loc[df["DeliveryTime"] > 60, "PerformanceFlag"] = "Delayed"
df.loc[df["DeliveryTime"].isna(), "PerformanceFlag"] = "Invalid / Missing"

summary = (
    df.groupby("Cuisine", dropna=False)
      .agg(
          Total_Revenue=("Revenue", "sum"),
          Average_DeliveryTime=("DeliveryTime", "mean"),
          Order_Count=("OrderID", "count"),
      )
      .reset_index()
)

# Revenue/DeliveryTime negative correlation would mean slower orders tend to be associated with lower revenue.
# DeliveryTime/Rating negative correlation would mean longer deliveries tend to reduce customer satisfaction.
# Revenue/Rating positive correlation would mean higher-value orders tend to receive higher ratings in this sample.
corr = df[["Revenue", "DeliveryTime", "Rating"]].corr()

print("=== Cuisine Summary ===")
print(summary.round(2).to_string(index=False))
print("\n=== IQR / Invalid Delivery-Time Check ===")
q1 = df["DeliveryTime"].quantile(0.25)
q3 = df["DeliveryTime"].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print(f"Q1={q1:.2f}, Q3={q3:.2f}, IQR={iqr:.2f}, Lower={lower:.2f}, Upper={upper:.2f}")
print(f"Invalid negative DeliveryTime rows fixed: {int(invalid_dt.sum())}")

print("\n=== Correlation Matrix ===")
print(corr.round(3).to_string())

with pd.ExcelWriter(OUTPUT_XLSX, engine="openpyxl") as writer:
    summary.to_excel(writer, sheet_name="Cuisine Summary", index=False)
    df.to_excel(writer, sheet_name="Enriched Data", index=False)
    corr.to_excel(writer, sheet_name="Correlation Matrix")

print(f"\nSaved: {OUTPUT_XLSX}")
