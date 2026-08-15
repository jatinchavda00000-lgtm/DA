import numpy as np
import matplotlib.pyplot as plt

# Weekly screen time (hours) for the past 8 weeks
screen_time = np.array([31, 34, 29, 36, 33, 35, 32, 52])

# Calculate quartiles and IQR
q1 = np.quantile(screen_time, 0.25)
q3 = np.quantile(screen_time, 0.75)
iqr = q3 - q1

# Find outliers using the IQR rule
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = screen_time[
    (screen_time < lower_bound) | (screen_time > upper_bound)
]

# Create boxplot and highlight outliers
plt.figure(figsize=(8, 5))
plt.boxplot(
    screen_time,
    vert=True,
    patch_artist=False,
    flierprops=dict(
        marker='o',
        markerfacecolor='red',
        markersize=8,
        markeredgecolor='red'
    )
)

plt.ylabel("Screen Time (Hours)")
plt.xlabel("Past 8 Weeks")
plt.title("Weekly Screen Time - Boxplot")
plt.xticks([1], ["Screen Time"])
plt.grid(axis="y", linestyle="--", alpha=0.5)

print("Weekly Screen Time:", screen_time)
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Outliers:", outliers)

plt.tight_layout()
plt.show()
