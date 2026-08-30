import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(7)
n = 200

df = pd.DataFrame({
    "order_value": np.random.uniform(100, 800, n),
    "distance_km": np.random.uniform(1, 20, n),
    "delivery_time_mins": np.random.normal(30, 8, n),
    "rating": np.random.uniform(1.0, 5.0, n),
    "discount_pct": np.random.uniform(0, 30, n),
})

for col in ["delivery_time_mins", "rating"]:
    null_indices = np.random.choice(df.index, size=int(0.05 * n), replace=False)
    df.loc[null_indices, col] = np.nan
    df[col] = df[col].fillna(df[col].median())

df["delivery_speed_kmph"] = df["distance_km"] / (df["delivery_time_mins"] / 60)
df["speed_band"] = pd.qcut(df["delivery_speed_kmph"], q=3, labels=["Slow", "Normal", "Fast"])

corr = df.select_dtypes(include=np.number).corr(method="pearson")
plt.figure(figsize=(9, 7))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0, vmin=-1, vmax=1)
plt.title("Food Delivery Pearson Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=200, bbox_inches="tight")
plt.close()

sns.pairplot(df[["order_value", "distance_km", "delivery_time_mins", "rating", "speed_band"]], hue="speed_band")
plt.savefig("pairplot.png", dpi=200, bbox_inches="tight")
plt.close()

print("TASK 4: FULL EDA PIPELINE")
print(f"Rows generated: {len(df)}")
print(f"Nulls after median fill: {int(df.isna().sum().sum())}")
print("Saved: correlation_heatmap.png (DPI 200)")
print("Saved: pairplot.png (DPI 200)")
print("Speed bands:")
print(df["speed_band"].value_counts().sort_index().to_string())
