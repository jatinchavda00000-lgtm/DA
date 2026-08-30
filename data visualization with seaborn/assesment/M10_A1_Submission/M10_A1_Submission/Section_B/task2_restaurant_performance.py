import numpy as np
import pandas as pd

np.random.seed(21)
restaurant_names = np.array(["Spice Route", "Urban Bites", "Dragon Bowl", "Pizza Hub", "Sweet Treats"])
cities = np.array(["Delhi", "Mumbai", "Bengaluru"])
cuisines = np.array(["Indian", "Chinese", "Desserts"])

n = 50
df = pd.DataFrame({
    "restaurant_name": np.random.choice(restaurant_names, n),
    "city": np.random.choice(cities, n),
    "order_value": np.round(np.random.uniform(150, 900, n), 2),
    "delivery_time_mins": np.round(np.random.uniform(20, 45, n), 1),
    "rating": np.round(np.random.uniform(3.4, 5.0, n), 1),
    "cuisine_type": np.random.choice(cuisines, n),
})

summary = (
    df.groupby("restaurant_name")
      .agg(
          mean_order_value=("order_value", "mean"),
          mean_delivery_time=("delivery_time_mins", "mean"),
          mean_rating=("rating", "mean"),
      )
      .query("mean_rating > 4.0 and mean_delivery_time < 35")
      .sort_values("mean_order_value", ascending=False)
      .reset_index()
)

summary["mean_order_value"] = summary["mean_order_value"].round(2)
summary["mean_delivery_time"] = summary["mean_delivery_time"].round(2)
summary["mean_rating"] = summary["mean_rating"].round(2)

print("TASK 2: RESTAURANT PERFORMANCE ANALYSER")
print(summary.to_string(index=False))
