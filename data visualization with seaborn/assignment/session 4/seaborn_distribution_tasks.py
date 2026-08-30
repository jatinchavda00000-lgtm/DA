import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

# ---------- Task 1: Flipkart ----------
flipkart_df = pd.read_csv("flipkart_prices.csv")
plt.figure(figsize=(9, 4))
sns.boxplot(x=flipkart_df["price"])
plt.title("Flipkart Product Price Distribution")
plt.xlabel("Price (₹)")
plt.show()

# ---------- Task 2: Zomato ----------
zomato_df = pd.read_csv("zomato_orders.csv")
plt.figure(figsize=(8, 5))
sns.violinplot(data=zomato_df, x="category", y="order_amount", inner="box")
plt.title("Zomato Order Amount Distribution: Fast Food vs Desserts")
plt.xlabel("Restaurant Category")
plt.ylabel("Order Amount (₹)")
plt.show()

# ---------- Task 3: IPL ----------
ipl_prices = np.array([
    500, 600, 700, 750, 800, 850, 900, 950, 1000, 1100,
    1200, 1250, 1300, 1400, 1500, 1600, 1800, 2000, 2200, 2500,
    6000
])

plt.figure(figsize=(10, 4))
sns.boxplot(x=ipl_prices)
plt.title("IPL Match Ticket Price Distribution")
plt.xlabel("Ticket Price (₹)")
plt.show()

q1 = np.percentile(ipl_prices, 25)
q3 = np.percentile(ipl_prices, 75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = ipl_prices[(ipl_prices < lower_bound) | (ipl_prices > upper_bound)]

print("IPL outliers:", outliers.tolist())

# ---------- Task 4: Fitness ----------
fitness_df = pd.read_csv("fitness_steps.csv")
plt.figure(figsize=(6, 6))
sns.violinplot(y=fitness_df["daily_steps"], inner="box")
plt.title("Daily Step Count Distribution")
plt.ylabel("Steps per Day")
plt.show()

print("Daily steps summary:")
print(fitness_df["daily_steps"].describe())
