import matplotlib.pyplot as plt

# ============================================================
# TASK 1
# Pie chart: Percentage of time spent on 5 apps in a day
# ============================================================

apps = ["Instagram", "YouTube", "WhatsApp", "Zomato", "Spotify"]
time_spent = [30, 25, 20, 15, 10]  # percentage of daily app usage

plt.figure(figsize=(7, 7))
plt.pie(
    time_spent,
    labels=apps,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Daily Time Spent on Apps")
plt.axis("equal")
plt.show()


# ============================================================
# TASK 2
# Pie chart: Monthly online spending across 4 categories
# Highlight the highest spending category using explode
# ============================================================

categories = ["Food Delivery", "Shopping", "Entertainment", "UPI Payments"]
spending = [3000, 5000, 2000, 4000]

# Shopping is the highest spending category, so it is exploded more.
explode = [0, 0.15, 0, 0]

plt.figure(figsize=(7, 7))
plt.pie(
    spending,
    labels=categories,
    autopct="%1.1f%%",
    explode=explode,
    startangle=90
)
plt.title("Monthly Online Spending Distribution")
plt.axis("equal")
plt.show()


# ============================================================
# TASK 3
# Convert the same spending pie chart into a donut chart
# using plt.Circle() and ax.add_artist()
# ============================================================

fig, ax = plt.subplots(figsize=(7, 7))

ax.pie(
    spending,
    labels=categories,
    autopct="%1.1f%%",
    explode=explode,
    startangle=90
)

# Add a white circle in the center to create the donut effect.
centre_circle = plt.Circle((0, 0), 0.70, fc="white")
ax.add_artist(centre_circle)

ax.set_title("Monthly Online Spending - Donut Chart")
ax.axis("equal")
plt.show()


# ============================================================
# TASK 4
# Donut chart: IPL Teams Instagram Followers Share
# Labels + autopct are both used as required.
# ============================================================

teams = ["Chennai Super Kings", "Mumbai Indians", "Royal Challengers Bengaluru", "Kolkata Knight Riders"]
followers = [15, 14, 13, 10]  # example follower counts in millions

fig, ax = plt.subplots(figsize=(8, 8))

ax.pie(
    followers,
    labels=teams,
    autopct="%1.1f%%",
    startangle=90
)

# Add white circle for donut effect.
centre_circle = plt.Circle((0, 0), 0.70, fc="white")
ax.add_artist(centre_circle)

ax.set_title("IPL Teams Instagram Followers Share")
ax.axis("equal")
plt.show()
