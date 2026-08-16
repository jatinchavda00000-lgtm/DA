import numpy as np

# Delivery times (in minutes) for 20 Zomato orders
delivery_times = np.array([
    25, 32, 28, 40, 35,
    30, 45, 27, 38, 42,
    33, 29, 50, 36, 31,
    26, 41, 34, 39, 37
])

# Calculate percentiles
p25 = np.percentile(delivery_times, 25)
p50 = np.percentile(delivery_times, 50)
p75 = np.percentile(delivery_times, 75)

print("Zomato Delivery Times:", delivery_times)
print("25th Percentile (P25):", p25)
print("50th Percentile (P50 / Median):", p50)
print("75th Percentile (P75):", p75)

print("\nInterpretation:")
print(f"25% of orders were delivered in about {p25:.1f} minutes or less.")
print(f"50% of orders were delivered in about {p50:.1f} minutes or less.")
print(f"75% of orders were delivered in about {p75:.1f} minutes or less.")
