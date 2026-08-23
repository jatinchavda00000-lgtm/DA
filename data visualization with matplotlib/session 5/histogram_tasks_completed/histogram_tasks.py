import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Histogram Practice Tasks 1–5
# ============================================================

# ---------------------------
# Task 1: Swiggy delivery times
# ---------------------------
delivery_times = [
    32, 28, 45, 30, 36, 40, 29, 34, 38, 31,
    27, 41, 33, 35, 39, 37, 44, 30, 29, 32,
    36, 28, 43, 31, 35, 40, 38, 33, 30, 42
]

plt.figure(figsize=(8, 5))
plt.hist(delivery_times, bins=8, edgecolor='black')
plt.title("Swiggy Delivery Time Distribution")
plt.xlabel("Delivery Time (minutes)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ---------------------------
# Task 2: IPL match scores
# ---------------------------
ipl_scores = np.array([
    128, 135, 142, 156, 168, 174, 181, 190, 205, 212,
    145, 152, 160, 171, 177, 185, 198, 203, 216, 220,
    132, 138, 149, 158, 165, 172, 180, 188, 195, 210,
    125, 140, 147, 154, 162, 169, 176, 184, 192, 207,
    130, 144, 151, 159, 167, 173, 179, 187, 200, 214,
    136, 146, 155, 164, 182, 196
])

for bins in [5, 10, 15]:
    plt.figure(figsize=(8, 5))
    plt.hist(ipl_scores, bins=bins, edgecolor='black')
    plt.title(f"IPL Match Scores Histogram (bins={bins})")
    plt.xlabel("Runs per Team")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

print("Task 2 observation:")
print("- bins=5: broader groups, smoother/simple overall shape, less detail.")
print("- bins=10: more detail becomes visible while the overall pattern stays clear.")
print("- bins=15: narrower groups reveal more variation, but the histogram can look more jagged.")
print("- More bins = more detail; fewer bins = more general/smoothed distribution.")

# ---------------------------
# Task 3: Daily step counts
# ---------------------------
step_counts = np.array([
    5200, 6800, 7400, 8100, 6300, 9200, 10500, 7100, 8600, 9700,
    11200, 5900, 7600, 8300, 9100, 6800, 7200, 9900, 10800, 6400,
    7800, 8700, 9500, 10200, 6100, 7300, 8000, 8900, 9800, 11500
])

# Frequency histogram (default)
plt.figure(figsize=(8, 5))
plt.hist(step_counts, bins=7, edgecolor='black')
plt.title("Daily Step Counts - Frequency")
plt.xlabel("Steps per Day")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Density histogram
plt.figure(figsize=(8, 5))
plt.hist(step_counts, bins=7, density=True, edgecolor='black')
plt.title("Daily Step Counts - Density")
plt.xlabel("Steps per Day")
plt.ylabel("Density")
plt.tight_layout()
plt.show()

print("\nTask 3 comparison:")
print("- Default plt.hist(): y-axis shows Frequency = number of days in each bin.")
print("- density=True: y-axis shows Density = normalized distribution.")
print("- With density=True, the total area of all bars is approximately 1.")
print("- Frequency answers 'how many days?'; density answers 'how concentrated is the data?'.")

# ---------------------------
# Task 4: Spotify song durations
# ---------------------------
np.random.seed(42)
song_durations = np.random.randint(120, 301, 50)

plt.figure(figsize=(8, 5))
plt.hist(song_durations, bins=8, color='purple', edgecolor='black')
plt.title("Spotify Song Duration Distribution")
plt.xlabel("Song Duration (seconds)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ---------------------------
# Task 5: Flipkart product prices
# ---------------------------
prices = np.array([
    120, 250, 499, 500, 510, 650, 800, 999, 1000,
    1050, 1200, 1500, 1999, 2000, 2100, 2500, 3200,
    4000, 5000
])

# Bin edges create these intervals:
# 100-500, 501-1000, 1001-2000, 2001-5000
# For continuous numeric data, use edges [100, 501, 1001, 2001, 5001]
bins = [100, 501, 1001, 2001, 5001]

plt.figure(figsize=(8, 5))
plt.hist(prices, bins=bins, edgecolor='black')
plt.title("Flipkart Product Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.xticks(bins)
plt.tight_layout()
plt.show()

print("\nTask 5 bin ranges:")
print("100–500")
print("501–1000")
print("1001–2000")
print("2001–5000")
