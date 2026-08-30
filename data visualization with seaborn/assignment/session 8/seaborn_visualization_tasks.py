# Seaborn Visualization Tasks
# Tasks:
# 1. Scatter plot: Instagram followers vs posts
# 2. Line plot: Daily Zomato food orders for 30 days
# 3. relplot: Movie ratings vs reviews by genre
# 4. regplot: YouTube hours vs exam scores + trend interpretation

import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set a clean Seaborn theme
sns.set_theme(style="whitegrid")

# ============================================================
# Task 1: Instagram Followers vs Number of Posts
# ============================================================

# Fictional data for 20 Instagram users
instagram_data = {
    "user": [f"User_{i}" for i in range(1, 21)],
    "followers": [
        120, 450, 800, 1500, 2300, 3100, 4200, 5600, 6800, 7500,
        8900, 10200, 12000, 14500, 16000, 18500, 21000, 24500, 28000, 32000
    ],
    "posts": [
        15, 28, 40, 55, 70, 82, 95, 110, 125, 140,
        155, 170, 185, 205, 225, 240, 265, 290, 320, 350
    ]
}

instagram_df = pd.DataFrame(instagram_data)

plt.figure(figsize=(9, 6))
sns.scatterplot(
    data=instagram_df,
    x="followers",
    y="posts",
    s=90
)
plt.title("Instagram Followers vs Number of Posts")
plt.xlabel("Number of Followers")
plt.ylabel("Number of Posts")
plt.tight_layout()
plt.show()


# ============================================================
# Task 2: Daily Zomato Food Orders for a Month
# ============================================================

# Use a reproducible random list of 30 order counts
random.seed(42)
orders = [random.randint(80, 300) for _ in range(30)]

zomato_df = pd.DataFrame({
    "day": list(range(1, 31)),
    "orders": orders
})

plt.figure(figsize=(11, 6))
sns.lineplot(
    data=zomato_df,
    x="day",
    y="orders",
    marker="o"
)
plt.title("Daily Number of Food Orders on Zomato")
plt.xlabel("Day of the Month")
plt.ylabel("Number of Food Orders")
plt.xticks(range(1, 31))
plt.tight_layout()
plt.show()

print("30 simulated Zomato order counts:")
print(orders)


# ============================================================
# Task 3: Movie Ratings vs Number of Reviews by Genre
# ============================================================

movie_data = {
    "movie": [
        "Movie_1", "Movie_2", "Movie_3", "Movie_4", "Movie_5",
        "Movie_6", "Movie_7", "Movie_8", "Movie_9", "Movie_10",
        "Movie_11", "Movie_12", "Movie_13", "Movie_14", "Movie_15"
    ],
    "rating": [
        8.2, 7.5, 6.9, 8.7, 7.8,
        6.5, 8.0, 7.2, 9.0, 6.8,
        8.4, 7.7, 6.3, 8.8, 7.0
    ],
    "reviews": [
        12000, 8500, 6200, 15000, 9800,
        4300, 11000, 7000, 18000, 5200,
        14000, 9000, 3800, 16500, 5600
    ],
    "genre": [
        "Action", "Comedy", "Drama", "Action", "Comedy",
        "Drama", "Action", "Comedy", "Drama", "Action",
        "Comedy", "Drama", "Action", "Comedy", "Drama"
    ]
}

movies_df = pd.DataFrame(movie_data)

sns.relplot(
    data=movies_df,
    x="rating",
    y="reviews",
    hue="genre",
    kind="scatter",
    height=6,
    aspect=1.4,
    s=100
)
plt.title("Movie Ratings vs Number of Reviews by Genre")
plt.xlabel("Movie Rating")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.show()


# ============================================================
# Task 4: YouTube Hours vs Exam Scores
# ============================================================

students_data = {
    "student": [f"Student_{i}" for i in range(1, 26)],
    "youtube_hours": [
        1.0, 1.5, 2.0, 2.5, 3.0,
        3.5, 4.0, 4.5, 5.0, 5.5,
        6.0, 6.5, 7.0, 7.5, 8.0,
        8.5, 9.0, 9.5, 10.0, 10.5,
        11.0, 11.5, 12.0, 12.5, 13.0
    ],
    "exam_score": [
        95, 92, 89, 87, 85,
        84, 82, 80, 78, 76,
        75, 73, 71, 69, 67,
        65, 63, 61, 59, 57,
        55, 53, 50, 48, 45
    ]
}

students_df = pd.DataFrame(students_data)

plt.figure(figsize=(9, 6))
sns.regplot(
    data=students_df,
    x="youtube_hours",
    y="exam_score",
    scatter_kws={"s": 70},
    line_kws={"linewidth": 2}
)
plt.title("YouTube Hours vs Exam Scores")
plt.xlabel("Hours Spent on YouTube")
plt.ylabel("Exam Score")
plt.tight_layout()
plt.show()

# Correlation coefficient
correlation = students_df["youtube_hours"].corr(students_df["exam_score"])

print("\nTask 4 Interpretation:")
print(f"Correlation coefficient: {correlation:.2f}")

if correlation > 0:
    print("The trend is POSITIVE: students spending more hours on YouTube tend to have higher exam scores.")
elif correlation < 0:
    print("The trend is NEGATIVE: students spending more hours on YouTube tend to have lower exam scores.")
else:
    print("There is NO clear linear trend between YouTube hours and exam scores.")

print("\nNote: This is simulated fictional data, so the correlation should not be treated as a real-world conclusion.")


# ============================================================
# Optional: Print all datasets
# ============================================================

print("\n--- Instagram Data ---")
print(instagram_df)

print("\n--- Zomato Data ---")
print(zomato_df)

print("\n--- Movie Data ---")
print(movies_df)

print("\n--- Student Data ---")
print(students_df)
