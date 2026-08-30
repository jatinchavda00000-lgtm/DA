"""
SESSION 11: Central Limit Theorem (CLT) Simulations
"""
import numpy as np
import matplotlib.pyplot as plt

print("="*60)
print("TASK 1 & 4: CLT Simulation (n=30 vs n=5 Sample Means)")
print("="*60)
np.random.seed(42)
# Highly skewed population: Instagram likes (Lognormal)
population_likes = np.random.lognormal(mean=4.0, sigma=1.2, size=50000)

sample_means_n30 = [np.mean(np.random.choice(population_likes, size=30, replace=False)) for _ in range(1000)]
sample_means_n5 = [np.mean(np.random.choice(population_likes, size=5, replace=False)) for _ in range(1000)]

fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

# Plot 1: Skewed Population
axes[0].hist(population_likes, bins=50, range=(0, 500), color='#E74C3C', alpha=0.7, edgecolor='black')
axes[0].set_title('Original Population (Highly Skewed)', fontweight='bold')
axes[0].set_xlabel('Instagram Likes')
axes[0].set_ylabel('Frequency')

# Plot 2: Sample Means n=5
axes[1].hist(sample_means_n5, bins=35, color='#F39C12', alpha=0.7, edgecolor='black')
axes[1].set_title('Sample Means (n = 5)', fontweight='bold')
axes[1].set_xlabel('Sample Mean Likes')

# Plot 3: Sample Means n=30
axes[2].hist(sample_means_n30, bins=35, color='#27AE60', alpha=0.7, edgecolor='black')
axes[2].set_title('Sample Means (n = 30) - CLT Normal', fontweight='bold')
axes[2].set_xlabel('Sample Mean Likes')

plt.tight_layout()
plt.savefig('session_11_clt_comparison.png', dpi=300)
plt.close()
print("Generated CLT multi-panel comparison plot: 'session_11_clt_comparison.png'.
")

print("="*60)
print("TASK 2 & 3: Analytical Explanation & Business Applications")
print("="*60)
print("Why Normality Emerges: When drawing random independent samples, positive and negative deviations average out. The distribution of aggregate means converges to a symmetric bell curve centered at the true population mean.")
print("E-Commerce Use Case (Flipkart): Even if customer cart values are heavily skewed with extreme outliers, sampling average order values daily ensures the daily averages follow a normal curve, enabling reliable confidence intervals for quarterly revenue projections.")
