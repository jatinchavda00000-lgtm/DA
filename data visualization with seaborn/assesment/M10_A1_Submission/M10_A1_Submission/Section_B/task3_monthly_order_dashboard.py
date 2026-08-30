import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)
months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
orders = np.random.randint(1000, 5001, 12)
avg_order_value = np.random.uniform(200, 400, 12)
revenue = orders * avg_order_value
delivery_mean, delivery_std = 28, 4
delivery_times = np.random.normal(delivery_mean, delivery_std, 500)

fig, axes = plt.subplots(1, 3, figsize=(19, 5))
fig.suptitle("Food Delivery Monthly Performance Dashboard", fontsize=15)

axes[0].plot(months, orders, marker="o")
for month, value in zip(months, orders):
    axes[0].annotate(str(value), (month, value), xytext=(0, 7), textcoords="offset points", ha="center")
axes[0].set_title("Monthly Total Orders")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Orders")

bar_colors = np.where(revenue > 800000, "green", "red")
axes[1].bar(months, revenue, color=bar_colors)
axes[1].axhline(800000, linestyle="--", linewidth=1.5, label="Rs 8,00,000 threshold")
axes[1].set_title("Monthly Revenue")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Revenue (Rs)")
axes[1].legend()

axes[2].hist(delivery_times, bins=15)
sample_mean = np.mean(delivery_times)
axes[2].axvline(sample_mean, linestyle="--", linewidth=1.5, label="Mean")
axes[2].set_title("Delivery Time Distribution")
axes[2].set_xlabel("Delivery Time (mins)")
axes[2].set_ylabel("Frequency")
axes[2].legend()

plt.tight_layout()
plt.savefig("food_delivery_dashboard.png", dpi=150, bbox_inches="tight")
print("TASK 3: MONTHLY ORDER TREND DASHBOARD")
print("Dashboard saved as food_delivery_dashboard.png at DPI 150.")
print(f"Sample delivery-time mean: {sample_mean:.2f} minutes")
