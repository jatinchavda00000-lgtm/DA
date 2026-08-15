import numpy as np

# IPL player scores
scores = np.array([
    12, 45, 67, 23, 89,
    56, 34, 78, 91, 15,
    42, 63, 37, 72, 28,
    50, 84, 19, 95, 61
])

# Calculate quartiles using numpy.quantile
q1 = np.quantile(scores, 0.25)
q2 = np.quantile(scores, 0.50)  # Median
q3 = np.quantile(scores, 0.75)

print("IPL Player Scores:", scores)
print("Q1 (25th Percentile):", q1)
print("Q2 (Median / 50th Percentile):", q2)
print("Q3 (75th Percentile):", q3)

print("\nInterpretation:")
print(f"Q1 = {q1:.2f}: 25% of scores are at or below this value.")
print(f"Q2 = {q2:.2f}: 50% of scores are at or below this value.")
print(f"Q3 = {q3:.2f}: 75% of scores are at or below this value.")
