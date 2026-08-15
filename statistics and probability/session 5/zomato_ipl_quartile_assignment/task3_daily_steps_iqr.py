import numpy as np

# Daily step counts for one month (30 days)
steps = np.array([
    6500, 7200, 8000, 6000, 9000, 7500, 8200, 6800, 7100, 7600,
    8400, 5900, 9300, 7000, 7800, 8100, 6700, 7400, 8600, 7200,
    6900, 8800, 6200, 7900, 7300, 8500, 6600, 9100, 7700, 7000
])

q1 = np.quantile(steps, 0.25)
q3 = np.quantile(steps, 0.75)
iqr = q3 - q1

print("Monthly Daily Step Counts:", steps)
print("Q1:", q1)
print("Q3:", q3)
print("Interquartile Range (IQR):", iqr)

print("\nInterpretation:")
print(
    f"The middle 50% of daily step counts lie between {q1:.0f} and {q3:.0f} steps."
)
print(
    f"The IQR is {iqr:.0f} steps, which shows the spread of the middle 50% of activity."
)
print(
    "A smaller IQR indicates more consistent daily activity, while a larger IQR "
    "indicates greater variation in daily activity."
)
