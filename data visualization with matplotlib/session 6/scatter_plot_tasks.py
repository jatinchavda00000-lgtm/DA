"""
Scatter Plot & Regression Tasks
Tasks 1-5 completed with fictional/sample data.

Requirements:
    pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# TASK 1
# Instagram hours per day vs posts uploaded per month
# ============================================================
def task1_instagram_scatter():
    users = [
        "User1", "User2", "User3", "User4", "User5",
        "User6", "User7", "User8", "User9", "User10"
    ]

    instagram_hours = np.array([0.8, 1.5, 2.0, 2.7, 3.1, 3.8, 4.2, 5.0, 5.8, 6.5])
    posts_per_month = np.array([2, 5, 8, 12, 16, 20, 25, 31, 37, 45])

    plt.figure(figsize=(8, 5))
    plt.scatter(instagram_hours, posts_per_month, s=80)
    plt.title("Instagram Usage vs Monthly Posts")
    plt.xlabel("Hours spent on Instagram per day")
    plt.ylabel("Number of posts uploaded per month")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("task1_instagram_scatter.png", dpi=150)
    plt.show()


# ============================================================
# TASK 2
# Zomato amount spent vs number of orders
# Label each point with friend's name using annotate()
# ============================================================
def task2_zomato_scatter():
    friends = [
        "Aarav", "Bhavya", "Chirag", "Diya",
        "Esha", "Farhan", "Gauri", "Harsh",
        "Isha", "Jay", "Kavya", "Mihir"
    ]

    amount_spent = np.array([900, 1200, 1500, 1800, 2100, 2500, 2800, 3200, 3600, 4000, 4500, 5000])
    orders = np.array([3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 17])

    plt.figure(figsize=(9, 6))
    plt.scatter(orders, amount_spent, s=90)

    for name, x, y in zip(friends, orders, amount_spent):
        plt.annotate(
            name,
            (x, y),
            xytext=(5, 5),
            textcoords="offset points",
            fontsize=9
        )

    plt.title("Zomato Orders vs Amount Spent")
    plt.xlabel("Number of orders placed")
    plt.ylabel("Amount spent on Zomato (₹)")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("task2_zomato_scatter.png", dpi=150)
    plt.show()


# ============================================================
# TASK 3
# Add best-fit trend line using numpy.polyfit()
# ============================================================
def task3_zomato_with_trendline():
    amount_spent = np.array([900, 1200, 1500, 1800, 2100, 2500, 2800, 3200, 3600, 4000, 4500, 5000])
    orders = np.array([3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 17])

    # polyfit degree=1 returns [slope, intercept]
    slope, intercept = np.polyfit(orders, amount_spent, 1)

    x_line = np.linspace(orders.min(), orders.max(), 100)
    y_line = slope * x_line + intercept

    plt.figure(figsize=(9, 6))
    plt.scatter(orders, amount_spent, s=90, label="Friends' data")
    plt.plot(x_line, y_line, linewidth=2, label="Best-fit trend line")

    plt.title("Zomato Orders vs Amount Spent with Trend Line")
    plt.xlabel("Number of orders placed")
    plt.ylabel("Amount spent on Zomato (₹)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("task3_zomato_trendline.png", dpi=150)
    plt.show()

    print(f"Task 3 equation: y = {slope:.2f}x + {intercept:.2f}")


# ============================================================
# TASK 4
# YouTube watch hours vs Spotify listening hours
# 15 users, regression line with equation printed on plot
# ============================================================
def task4_youtube_spotify_regression():
    users = [
        "U1", "U2", "U3", "U4", "U5",
        "U6", "U7", "U8", "U9", "U10",
        "U11", "U12", "U13", "U14", "U15"
    ]

    youtube_hours = np.array([4, 6, 7, 9, 11, 13, 15, 16, 18, 20, 22, 24, 26, 28, 30])
    spotify_hours = np.array([8, 10, 13, 14, 17, 20, 21, 25, 27, 29, 33, 35, 38, 40, 43])

    slope, intercept = np.polyfit(youtube_hours, spotify_hours, 1)

    x_line = np.linspace(youtube_hours.min(), youtube_hours.max(), 100)
    y_line = slope * x_line + intercept

    equation = f"y = {slope:.2f}x + {intercept:.2f}"

    plt.figure(figsize=(9, 6))
    plt.scatter(youtube_hours, spotify_hours, s=85, label="Users' data")
    plt.plot(x_line, y_line, linewidth=2, label="Regression line")

    plt.title("YouTube Watch Hours vs Spotify Listening Hours")
    plt.xlabel("YouTube watch hours")
    plt.ylabel("Spotify listening hours")
    plt.text(
        0.05, 0.95,
        equation,
        transform=plt.gca().transAxes,
        fontsize=12,
        verticalalignment="top",
        bbox=dict(boxstyle="round", alpha=0.15)
    )
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("task4_youtube_spotify_regression.png", dpi=150)
    plt.show()

    print(f"Task 4 equation: {equation}")


# ============================================================
# TASK 5
# Generated-code style solution:
# Flipkart orders vs total amount spent for 10 users.
# Regression line using numpy.polyfit().
#
# Note on changes:
# - Used numpy arrays for clean numerical calculations.
# - Added np.polyfit(..., 1) for the linear regression line.
# - Used np.linspace() so the trend line appears smooth.
# - Added labels, legend, grid, and tight_layout() for readability.
# ============================================================
def task5_flipkart_regression():
    users = [
        "User1", "User2", "User3", "User4", "User5",
        "User6", "User7", "User8", "User9", "User10"
    ]

    flipkart_orders = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    total_spent = np.array([1200, 2100, 2800, 3900, 5100, 6200, 7600, 8700, 9900, 11500])

    slope, intercept = np.polyfit(flipkart_orders, total_spent, 1)

    x_line = np.linspace(flipkart_orders.min(), flipkart_orders.max(), 100)
    y_line = slope * x_line + intercept

    plt.figure(figsize=(9, 6))
    plt.scatter(
        flipkart_orders,
        total_spent,
        s=90,
        label="Users' data"
    )
    plt.plot(
        x_line,
        y_line,
        linewidth=2,
        label="Regression line"
    )

    plt.title("Flipkart Orders vs Total Amount Spent")
    plt.xlabel("Number of Flipkart orders")
    plt.ylabel("Total amount spent (₹)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("task5_flipkart_regression.png", dpi=150)
    plt.show()

    print(f"Task 5 equation: y = {slope:.2f}x + {intercept:.2f}")


def main():
    # Run all tasks one by one.
    task1_instagram_scatter()
    task2_zomato_scatter()
    task3_zomato_with_trendline()
    task4_youtube_spotify_regression()
    task5_flipkart_regression()


if __name__ == "__main__":
    main()
