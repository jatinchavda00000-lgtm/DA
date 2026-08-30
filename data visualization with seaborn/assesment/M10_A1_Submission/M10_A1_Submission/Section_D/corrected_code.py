import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
n = 180

df = pd.DataFrame({
    "order_value": np.random.uniform(100, 800, n),
    "distance_km": np.random.uniform(1, 20, n),
    "delivery_time_mins": np.random.normal(30, 6, n),
    "rating": np.random.uniform(1, 5, n),
    "discount_pct": np.random.uniform(0, 30, n),
    "restaurant_age_years": np.random.uniform(1, 12, n),
    "cuisine_type": np.random.choice(["Indian", "Chinese", "Fast Food", "Desserts"], n),
})

# Improvement: make plotting deterministic and save the pairplot explicitly.
g = sns.pairplot(df, hue="cuisine_type", diag_kind="hist")
g.savefig("ai_corrected_pairplot.png", dpi=200, bbox_inches="tight")
plt.close(g.fig)

# Fix: select only numeric columns before Pearson correlation.
numeric_df = df.select_dtypes(include=np.number)
corr = numeric_df.corr(method="pearson")

plt.figure(figsize=(9, 7))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0, vmin=-1, vmax=1)
plt.title("Food Delivery Pearson Correlation Heatmap")
plt.tight_layout()
plt.savefig("ai_corrected_correlation_heatmap.png", dpi=200, bbox_inches="tight")
plt.close()

print("Corrected Section D code completed successfully.")
print("Pairplot: ai_corrected_pairplot.png (DPI 200)")
print("Heatmap: ai_corrected_correlation_heatmap.png (DPI 200)")
