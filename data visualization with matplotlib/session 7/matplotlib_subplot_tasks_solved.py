import matplotlib.pyplot as plt
import numpy as np

# =========================
# Task 1
# =========================
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [6500, 7200, 8100, 7000, 9000, 10500, 8500]
water_litres = [2.0, 2.3, 2.1, 2.5, 2.8, 3.0, 2.4]

plt.figure(figsize=(10, 7))

plt.subplot(2, 1, 1)
plt.plot(days, steps, marker="o")
plt.title("Daily Step Count")
plt.ylabel("Steps")

plt.subplot(2, 1, 2)
plt.plot(days, water_litres, marker="o")
plt.title("Daily Water Intake")
plt.xlabel("Day")
plt.ylabel("Litres")

plt.tight_layout()
plt.show()


# =========================
# Task 2
# =========================
quarters = ["Q1", "Q2", "Q3", "Q4"]
instagram_posts = [45, 60, 52, 70]

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

axes[0, 0].plot(quarters, instagram_posts, marker="o")
axes[0, 0].set_title("Instagram Posts — Line")
axes[0, 0].set_ylabel("Posts")

axes[0, 1].bar(quarters, instagram_posts)
axes[0, 1].set_title("Instagram Posts — Bar")
axes[0, 1].set_ylabel("Posts")

axes[1, 0].scatter(quarters, instagram_posts, s=100)
axes[1, 0].set_title("Instagram Posts — Scatter")
axes[1, 0].set_ylabel("Posts")

axes[1, 1].pie(
    instagram_posts,
    labels=quarters,
    autopct="%1.1f%%",
    startangle=90
)
axes[1, 1].set_title("Instagram Posts — Pie")

fig.suptitle("Instagram Posts by Quarter", fontsize=16)
plt.tight_layout()
plt.show()


# =========================
# Task 3
# =========================
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

zomato_orders = [8, 6, 7, 10, 9, 11]
swiggy_orders = [5, 7, 6, 8, 10, 9]
dominos_orders = [3, 4, 5, 4, 6, 7]

fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)

axes[0].plot(months, zomato_orders, marker="o")
axes[0].set_title("Zomato")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Number of Orders")

axes[1].plot(months, swiggy_orders, marker="o")
axes[1].set_title("Swiggy")
axes[1].set_xlabel("Month")

axes[2].plot(months, dominos_orders, marker="o")
axes[2].set_title("Domino's")
axes[2].set_xlabel("Month")

fig.suptitle("Food Orders Over the Last 6 Months", fontsize=16)
plt.tight_layout()
plt.show()


# =========================
# Task 4
# =========================
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

youtube_gb = [12, 15, 18, 20, 22, 19]
instagram_gb = [6, 7, 8, 9, 10, 11]
spotify_gb = [4, 5, 4.5, 6, 5.5, 6.5]
whatsapp_gb = [2, 2.5, 3, 2.8, 3.2, 3.5]

fig, axes = plt.subplots(2, 2, figsize=(12, 9), sharex=True)

axes[0, 0].plot(months, youtube_gb, marker="o")
axes[0, 0].set_title("YouTube")
axes[0, 0].set_ylabel("Data Usage (GB)")

axes[0, 1].plot(months, instagram_gb, marker="o")
axes[0, 1].set_title("Instagram")
axes[0, 1].set_ylabel("Data Usage (GB)")

axes[1, 0].plot(months, spotify_gb, marker="o")
axes[1, 0].set_title("Spotify")
axes[1, 0].set_xlabel("Month")
axes[1, 0].set_ylabel("Data Usage (GB)")

axes[1, 1].plot(months, whatsapp_gb, marker="o")
axes[1, 1].set_title("WhatsApp")
axes[1, 1].set_xlabel("Month")
axes[1, 1].set_ylabel("Data Usage (GB)")

fig.suptitle("Monthly Mobile Data Usage by App", fontsize=16)
plt.tight_layout()
plt.show()
