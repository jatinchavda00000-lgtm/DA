import matplotlib.pyplot as plt

# Daily steps for the past 7 days
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [6500, 7200, 8100, 5600, 9000, 10500, 7800]

plt.figure(figsize=(8, 5))
plt.plot(days, steps, marker="o", linewidth=2)

plt.xlabel("Day")
plt.ylabel("Number of Steps")
plt.title("Daily Steps - Last 7 Days")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
