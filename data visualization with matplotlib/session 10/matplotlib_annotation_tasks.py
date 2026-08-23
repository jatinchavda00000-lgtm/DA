import matplotlib.pyplot as plt

# ============================================================
# Task 1: Daily Active Users over 12 Months - Line Chart
# ============================================================

months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

daily_active_users = [12000, 13500, 12800, 14500, 15200, 16800,
                      17500, 18300, 17100, 19500, 21000, 20500]

highest_index = daily_active_users.index(max(daily_active_users))

plt.figure(figsize=(10, 6))
plt.plot(months, daily_active_users, marker="o", linewidth=2)
plt.title("Monthly Daily Active Users - Music Streaming App")
plt.xlabel("Month")
plt.ylabel("Daily Active Users")
plt.grid(True, alpha=0.3)

plt.annotate(
    f"Highest: {daily_active_users[highest_index]:,}",
    xy=(months[highest_index], daily_active_users[highest_index]),
    xytext=(months[highest_index - 2], daily_active_users[highest_index] + 2500),
    arrowprops=dict(arrowstyle="->", linewidth=1.5),
    fontsize=10
)

plt.tight_layout()
plt.show()


# ============================================================
# Task 2: Monthly Orders - Bar Chart with Lowest-Order Arrow
# ============================================================

orders = [8500, 9200, 7800, 10500, 11200, 9800,
          12500, 11800, 8900, 13200, 14500, 13800]

lowest_index = orders.index(min(orders))

plt.figure(figsize=(10, 6))
bars = plt.bar(months, orders)
plt.title("Monthly Orders - Food Delivery App")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.grid(axis="y", alpha=0.3)

plt.annotate(
    f"Lowest: {orders[lowest_index]:,}",
    xy=(lowest_index, orders[lowest_index]),
    xytext=(lowest_index + 1.2, orders[lowest_index] + 2500),
    arrowprops=dict(arrowstyle="->", linewidth=1.5),
    fontsize=10,
    ha="center"
)

plt.tight_layout()
plt.show()


# ============================================================
# Task 3: Payment Methods - Pie Chart with Lower-Right Legend
# ============================================================

payment_methods = ["UPI", "Card", "Wallet", "Cash"]
payment_percentages = [55, 25, 12, 8]

plt.figure(figsize=(8, 7))
plt.pie(
    payment_percentages,
    labels=payment_methods,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Payment Method Usage - E-commerce App")
plt.legend(
    payment_methods,
    title="Payment Methods",
    loc="lower right"
)
plt.tight_layout()
plt.show()


# ============================================================
# Task 4: Movie Ratings vs Reviews - Scatter Plot
# Add a text box highlighting the highest-rated movie
# ============================================================

movies = [
    "Movie A", "Movie B", "Movie C", "Movie D", "Movie E",
    "Movie F", "Movie G", "Movie H", "Movie I", "Movie J"
]

ratings = [7.2, 8.1, 6.9, 9.3, 7.8, 8.7, 6.5, 9.5, 8.0, 7.4]
reviews = [1500, 2800, 1200, 4200, 2300, 3500, 900, 5000, 2600, 1800]

highest_rating_index = ratings.index(max(ratings))

plt.figure(figsize=(10, 6))
plt.scatter(reviews, ratings, s=80)
plt.title("Movie Ratings vs Number of Reviews")
plt.xlabel("Number of Reviews")
plt.ylabel("Movie Rating")
plt.grid(True, alpha=0.3)

plt.annotate(
    f"Highest Rated: {movies[highest_rating_index]} ({ratings[highest_rating_index]})",
    xy=(reviews[highest_rating_index], ratings[highest_rating_index]),
    xytext=(reviews[highest_rating_index] - 1800,
            ratings[highest_rating_index] - 0.6),
    bbox=dict(boxstyle="round,pad=0.5", edgecolor="black", facecolor="white"),
    arrowprops=dict(arrowstyle="->", linewidth=1.5),
    fontsize=10
)

plt.tight_layout()
plt.show()
