import matplotlib.pyplot as plt

# ============================================================
# Matplotlib Practice Tasks - Completed
# ============================================================

# ------------------------------------------------------------
# Task 1: Daily Active Users on a Music Streaming App
# Figure size: 10 inches wide x 4 inches tall using plt.figure()
# ------------------------------------------------------------
days_7 = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
daily_active_users = [12000, 13500, 12800, 14500, 15200, 18000, 19500]

plt.figure(figsize=(10, 4))
plt.plot(days_7, daily_active_users, marker="o", linewidth=2)
plt.title("Daily Active Users - Music Streaming App")
plt.xlabel("Day")
plt.ylabel("Daily Active Users")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# Task 2: Zomato vs Swiggy Food Orders
# Different line styles + legend
# ------------------------------------------------------------
zomato_orders = [220, 250, 240, 280, 300, 360, 390]
swiggy_orders = [210, 235, 255, 270, 290, 340, 375]

plt.figure(figsize=(10, 5))
plt.plot(
    days_7,
    zomato_orders,
    linestyle="--",
    marker="o",
    linewidth=2,
    label="Zomato"
)
plt.plot(
    days_7,
    swiggy_orders,
    linestyle=":",
    marker="s",
    linewidth=2,
    label="Swiggy"
)
plt.title("Weekly Food Orders: Zomato vs Swiggy")
plt.xlabel("Day")
plt.ylabel("Number of Food Orders")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# Task 3: Flipkart Daily Sales for 10 Days
# Use ggplot style + orange line
# ------------------------------------------------------------
flipkart_days = [
    "Day 1", "Day 2", "Day 3", "Day 4", "Day 5",
    "Day 6", "Day 7", "Day 8", "Day 9", "Day 10"
]
flipkart_sales = [420, 460, 440, 500, 540, 580, 620, 600, 670, 720]

plt.style.use("ggplot")

plt.figure(figsize=(10, 5))
plt.plot(
    flipkart_days,
    flipkart_sales,
    color="orange",
    marker="o",
    linewidth=2
)
plt.title("Flipkart Daily Sales - 10 Days")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# Task 4: Instagram Branding Palette - Daily Posts
# Bar chart with a list of hex colors
# ------------------------------------------------------------
instagram_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
instagram_posts = [180, 220, 195, 260, 300, 350, 320]

# Instagram-inspired pink/purple/orange palette
instagram_colors = [
    "#833AB4",  # Purple
    "#C13584",  # Magenta
    "#E1306C",  # Pink
    "#FD1D1D",  # Red
    "#F56040",  # Coral
    "#FCAF45",  # Orange
    "#FFDC80"   # Yellow
]

plt.style.use("default")

plt.figure(figsize=(10, 5))
plt.bar(
    instagram_days,
    instagram_posts,
    color=instagram_colors
)
plt.title("Instagram - Daily Posts Uploaded")
plt.xlabel("Day")
plt.ylabel("Number of Posts")
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# Task 5: Dark Theme Restyling
# Restyle Task 1 using dark_background.
# Constraint: colors are different from the original chart.
# ------------------------------------------------------------
plt.style.use("dark_background")

plt.figure(figsize=(10, 4))
plt.plot(
    days_7,
    daily_active_users,
    color="#00FFFF",      # Different from Task 1 default line color
    marker="o",
    markerfacecolor="#FFD700",
    markeredgecolor="white",
    linewidth=2.5
)
plt.title("Daily Active Users - Dark Theme")
plt.xlabel("Day")
plt.ylabel("Daily Active Users")
plt.grid(True, alpha=0.25)
plt.tight_layout()
plt.show()

# Reset style after completing all tasks
plt.style.use("default")
