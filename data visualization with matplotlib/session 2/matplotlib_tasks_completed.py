import matplotlib.pyplot as plt

# Task 1: Daily steps
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [6500, 8200, 7100, 9000, 7800, 10500, 8800]

plt.figure(figsize=(8, 5))
plt.plot(days, steps, color="green", linewidth=2)
plt.title("Daily Steps Over the Last 7 Days")
plt.xlabel("Day")
plt.ylabel("Steps")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Task 2: Music app monthly active users
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
monthly_active_users = [120, 135, 150, 148, 165, 180]

plt.figure(figsize=(8, 5))
plt.plot(months, monthly_active_users, marker="o", markerfacecolor="red")
plt.title("Monthly Active Users")
plt.xlabel("Month")
plt.ylabel("Users (Millions)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Task 3: Zomato vs Swiggy orders
months_5 = ["Feb", "Mar", "Apr", "May", "Jun"]
zomato_orders = [12, 15, 14, 18, 20]
swiggy_orders = [10, 13, 16, 17, 19]

plt.figure(figsize=(8, 5))
plt.plot(
    months_5, zomato_orders,
    color="blue", linestyle="-", linewidth=2, label="Zomato"
)
plt.plot(
    months_5, swiggy_orders,
    color="orange", linestyle="--", linewidth=2, label="Swiggy"
)
plt.title("Monthly Orders: Zomato vs Swiggy")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Task 4: Mobile data usage
months_6 = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
data_used = [12, 15, 18, 16, 21, 24]

plt.figure(figsize=(8, 5))
plt.plot(months_6, data_used, marker="o", linewidth=2)
plt.title("Monthly Data Usage Trend")
plt.xlabel("Month")
plt.ylabel("Data Used (GB)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
