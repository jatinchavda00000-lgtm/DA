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

sns.pairplot(df, hue="cuisine_type")
plt.savefig("ai_pairplot.png")

corr = df.corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Food Delivery Correlation Heatmap")
plt.savefig("ai_correlation_heatmap.png")
