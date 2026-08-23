import matplotlib.pyplot as plt

# ============================================================
# Task 1 + Task 3 + Task 4
# Food Delivery Apps - Vertical Bar Chart
# ============================================================

apps = ["Zomato", "Swiggy", "Uber Eats", "Dunzo", "Domino's"]
orders = [12000, 15000, 8000, 5000, 10000]

# Custom color for each bar
colors = ["red", "orange", "green", "blue", "purple"]

plt.figure(figsize=(10, 6))

# Task 4: thinner bars using width < 0.8
bars = plt.bar(apps, orders, color=colors, width=0.55)

plt.title("Daily Orders for Popular Food Delivery Apps")
plt.xlabel("Food Delivery Apps")
plt.ylabel("Number of Daily Orders")

# Task 3: exact order count above each bar using plt.text()
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{int(height)}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.show()


# ============================================================
# Task 2
# Instagram Influencers - Horizontal Bar Chart
# ============================================================

influencers = [
    "Influencer A",
    "Influencer B",
    "Influencer C",
    "Influencer D",
    "Influencer E",
    "Influencer F"
]

followers = [12, 18, 25, 10, 30, 15]  # Followers in millions

plt.figure(figsize=(10, 6))

plt.barh(influencers, followers)

plt.title("Instagram Influencers by Followers")
plt.xlabel("Followers (in millions)")
plt.ylabel("Instagram Influencers")

plt.tight_layout()
plt.show()
