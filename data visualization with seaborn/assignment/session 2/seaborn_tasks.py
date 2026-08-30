# Seaborn Tasks: Swiggy, Zomato & BookMyShow-style datasets
# ---------------------------------------------------------------
# Requirements:
#   pip install pandas seaborn matplotlib

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# General plot settings
sns.set_theme(style="whitegrid")

# ===============================================================
# Task 1
# Use sns.countplot() to visualize the number of orders placed
# by each payment method (at least 3 payment types).
# ===============================================================

swiggy_df = pd.DataFrame({
    "order_id": range(1, 13),
    "payment_method": [
        "UPI", "Card", "Cash", "UPI", "Card", "UPI",
        "Cash", "UPI", "Card", "Cash", "UPI", "Card"
    ],
    "food_category": [
        "Pizza", "Burger", "Biryani", "Pizza", "South Indian", "Burger",
        "Pizza", "Biryani", "Burger", "South Indian", "Pizza", "Biryani"
    ]
})

plt.figure(figsize=(7, 5))
sns.countplot(data=swiggy_df, x="payment_method")
plt.title("Task 1: Number of Orders by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.show()


# ===============================================================
# Task 2
# Use sns.barplot() with estimator=mean to show the average
# delivery time for each food category.
# ===============================================================

zomato_df = pd.DataFrame({
    "order_id": range(1, 13),
    "food_category": [
        "Pizza", "Burger", "Biryani", "South Indian",
        "Pizza", "Burger", "Biryani", "South Indian",
        "Pizza", "Burger", "Biryani", "South Indian"
    ],
    "delivery_time": [
        35, 28, 42, 30,
        40, 25, 45, 32,
        38, 30, 40, 34
    ]
})

plt.figure(figsize=(8, 5))
sns.barplot(
    data=zomato_df,
    x="food_category",
    y="delivery_time",
    estimator="mean"
)
plt.title("Task 2: Average Delivery Time by Food Category")
plt.xlabel("Food Category")
plt.ylabel("Average Delivery Time (minutes)")
plt.tight_layout()
plt.show()


# ===============================================================
# Task 3
# Modify the barplot to display the total number of orders
# instead of the average by setting estimator="sum".
#
# We add an order_count column with value 1 per order, so summing
# it gives the total number of orders in each category.
# ===============================================================

zomato_df["order_count"] = 1

plt.figure(figsize=(8, 5))
sns.barplot(
    data=zomato_df,
    x="food_category",
    y="order_count",
    estimator="sum"
)
plt.title("Task 3: Total Number of Orders by Food Category")
plt.xlabel("Food Category")
plt.ylabel("Total Number of Orders")
plt.tight_layout()
plt.show()


# ===============================================================
# Task 4
# Plot a countplot of movie genres from a BookMyShow-style dataset.
#
# Note:
# countplot() itself does not use a confidence interval, so there
# is no ci parameter to remove. The hint mentioning ci=None applies
# to barplot() in older Seaborn usage. For a true countplot, simply
# use sns.countplot() (no confidence interval is displayed).
# ===============================================================

bookmyshow_df = pd.DataFrame({
    "movie": [
        "Movie A", "Movie B", "Movie C", "Movie D", "Movie E",
        "Movie F", "Movie G", "Movie H", "Movie I", "Movie J",
        "Movie K", "Movie L"
    ],
    "genre": [
        "Action", "Comedy", "Drama", "Action", "Comedy", "Action",
        "Thriller", "Drama", "Comedy", "Action", "Thriller", "Drama"
    ]
})

plt.figure(figsize=(8, 5))
sns.countplot(data=bookmyshow_df, x="genre")
plt.title("Task 4: Number of Movies by Genre")
plt.xlabel("Movie Genre")
plt.ylabel("Count")
plt.tight_layout()
plt.show()


# ===============================================================
# Optional: print sample data and summary results
# ===============================================================

print("\n--- Swiggy-style dataset ---")
print(swiggy_df)

print("\n--- Zomato-style dataset ---")
print(zomato_df)

print("\n--- Average delivery time by category ---")
print(
    zomato_df.groupby("food_category", as_index=False)["delivery_time"]
    .mean()
)

print("\n--- Total orders by category ---")
print(
    zomato_df.groupby("food_category")["order_count"]
    .sum()
)

print("\n--- BookMyShow-style genre counts ---")
print(bookmyshow_df["genre"].value_counts())
