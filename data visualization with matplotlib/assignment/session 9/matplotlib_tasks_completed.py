import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# ============================================================
# Task 1: Stacked Bar Chart - Zomato & Swiggy Food Orders
# ============================================================

days = ["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"]

zomato_orders = np.array([35, 42, 38, 45, 50, 65, 58])
swiggy_orders = np.array([30, 36, 40, 39, 48, 60, 55])

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(days, zomato_orders, label="Zomato")
ax.bar(days, swiggy_orders, bottom=zomato_orders, label="Swiggy")

ax.set_title("Daily Food Orders - Zomato vs Swiggy")
ax.set_xlabel("Day of the Week")
ax.set_ylabel("Number of Orders")
ax.legend()
ax.grid(axis="y", linestyle="--", alpha=0.3)

plt.xticks(rotation=20)
plt.tight_layout()
plt.show()


# ============================================================
# Task 2: Area Chart - Spotify & YouTube Daily Active Users
# ============================================================

days_7 = np.arange(1, 8)

spotify_users = np.array([120, 135, 128, 145, 150, 165, 172])
youtube_users = np.array([180, 190, 185, 200, 210, 225, 235])

fig, ax = plt.subplots(figsize=(10, 6))

ax.fill_between(
    days_7,
    spotify_users,
    alpha=0.5,
    label="Spotify"
)

ax.fill_between(
    days_7,
    youtube_users,
    alpha=0.35,
    label="YouTube"
)

ax.plot(days_7, spotify_users, marker="o")
ax.plot(days_7, youtube_users, marker="o")

ax.set_title("Daily Active Users - Spotify vs YouTube")
ax.set_xlabel("Day")
ax.set_ylabel("Daily Active Users (Thousands)")
ax.legend()

ax.set_xticks(days_7)
plt.tight_layout()
plt.show()


# ============================================================
# Task 3: Error Bar Chart - Flipkart Average Delivery Time
# ============================================================

days_10 = np.arange(1, 11)

delivery_time = np.array([
    42, 45, 40, 47, 43, 50, 46, 44, 48, 45
])

std_deviation = np.array([
    4, 3, 5, 4, 3, 6, 4, 5, 3, 4
])

fig, ax = plt.subplots(figsize=(10, 6))

ax.errorbar(
    days_10,
    delivery_time,
    yerr=std_deviation,
    fmt="o-",
    capsize=5,
    label="Flipkart Delivery Time"
)

ax.set_title("Average Flipkart Delivery Time with Standard Deviation")
ax.set_xlabel("Day")
ax.set_ylabel("Delivery Time (Minutes)")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.3)

ax.set_xticks(days_10)
plt.tight_layout()
plt.show()


# ============================================================
# Task 4: Time Series Line Chart - Paytm Wallet Balance
# ============================================================

start_date = datetime.today() - timedelta(days=13)
dates = [start_date + timedelta(days=i) for i in range(14)]

paytm_balance = np.array([
    4200, 4050, 4380, 4300, 4550, 4475, 4700,
    4620, 4890, 4750, 5100, 4980, 5250, 5400
])

fig, ax = plt.subplots(figsize=(11, 6))

ax.plot(
    dates,
    paytm_balance,
    marker="o",
    linewidth=2,
    label="Paytm Wallet Balance"
)

ax.set_title("Paytm Wallet Balance - Last 14 Days")
ax.set_xlabel("Date")
ax.set_ylabel("Wallet Balance (₹)")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.3)

# Format x-axis as DD MMM, e.g. 12 Jun
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
fig.autofmt_xdate()

plt.tight_layout()
plt.show()


# ============================================================
# Task 5: Dashboard-Style Area Chart
# Constraint:
# Use ax.set_title(), ax.set_xlabel(), ax.set_ylabel(),
# and ax.grid(True)
# ============================================================

dashboard_days = np.arange(1, 8)

instagram_reach = np.array([1200, 1450, 1380, 1600, 1750, 1900, 2150])

fig, ax = plt.subplots(figsize=(11, 6))

ax.fill_between(
    dashboard_days,
    instagram_reach,
    alpha=0.45,
    label="Instagram Reach"
)

ax.plot(
    dashboard_days,
    instagram_reach,
    marker="o",
    linewidth=2,
    label="Daily Reach"
)

# Required statements
ax.set_title("Instagram Insights - Weekly Reach")
ax.set_xlabel("Day")
ax.set_ylabel("Reach")
ax.grid(True, linestyle="--", alpha=0.35)

ax.set_xticks(dashboard_days)
ax.legend()

plt.tight_layout()
plt.show()


# ============================================================
# End of Tasks
# ============================================================
print("All 5 Matplotlib tasks completed successfully!")
