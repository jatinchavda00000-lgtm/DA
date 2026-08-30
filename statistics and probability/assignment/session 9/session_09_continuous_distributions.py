"""
SESSION 9: Continuous Probability Distributions (Normal Distribution & Z-Scores)
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

print("="*60)
print("TASK 1: Generate & Plot 1000 Normal Random Numbers (μ=500, σ=100)")
print("="*60)
np.random.seed(42)
data_norm = np.random.normal(loc=500, scale=100, size=1000)
plt.figure(figsize=(8, 4.5))
plt.hist(data_norm, bins=30, density=True, alpha=0.6, color='#3498DB', edgecolor='black')
xmin, xmax = plt.xlim()
x_axis = np.linspace(xmin, xmax, 200)
plt.plot(x_axis, stats.norm.pdf(x_axis, 500, 100), 'r-', linewidth=2, label='Normal Curve PDF')
plt.title('Simulated Normal Distribution (μ=500, σ=100, N=1000)', fontsize=12, fontweight='bold')
plt.xlabel('Values', fontsize=10)
plt.ylabel('Density', fontsize=10)
plt.legend()
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.savefig('session_09_task1_normal_dist.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved Task 1 plot as 'session_09_task1_normal_dist.png'.
")

print("="*60)
print("TASK 2: Z-Score Calculation for 9,500 Daily Steps")
print("="*60)
mu_steps = 8000
sigma_steps = 1200
x_steps = 9500
z_steps = (x_steps - mu_steps) / sigma_steps
print(f"Observed Steps (x) = {x_steps} | Mean (μ) = {mu_steps} | Std Dev (σ) = {sigma_steps}")
print(f"Z-Score = (9500 - 8000) / 1200 = {z_steps:.4f}")
print(f"Interpretation: The step count is +1.25 standard deviations above the population average.
")

print("="*60)
print("TASK 3: Standard Normal Curve with Shaded [-1, 1] Region")
print("="*60)
x_std = np.linspace(-4, 4, 1000)
y_std = stats.norm.pdf(x_std, 0, 1)
plt.figure(figsize=(8, 4.5))
plt.plot(x_std, y_std, color='black', linewidth=1.5, label='Standard Normal (μ=0, σ=1)')
plt.fill_between(x_std, y_std, where=(x_std >= -1) & (x_std <= 1), color='#58D68D', alpha=0.6, label='P(-1 ≤ Z ≤ 1) ≈ 68.27%')
plt.title('Standard Normal Curve with ±1σ Shaded Region', fontsize=12, fontweight='bold')
plt.xlabel('Z-Score', fontsize=10)
plt.ylabel('Probability Density', fontsize=10)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.savefig('session_09_task3_standard_normal.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved Task 3 plot as 'session_09_task3_standard_normal.png'.
")

print("="*60)
print("TASK 4: Zomato Delivery Time Under 25 Minutes (CDF)")
print("="*60)
mu_del = 30
sigma_del = 5
prob_under_25 = stats.norm.cdf(25, loc=mu_del, scale=sigma_del)
print(f"Mean Delivery Time = {mu_del} mins | Std Dev = {sigma_del} mins")
print(f"P(Time < 25 mins) = stats.norm.cdf(25, 30, 5) = {prob_under_25:.4f} ({prob_under_25*100:.2f}%)
")

print("="*60)
print("TASK 5: Analytical Importance of Normal Distribution")
print("="*60)
print("In enterprise analytics, large natural variations in delivery logistics, order amounts, and user engagement tend toward normality due to aggregate underlying processes, enabling standardized thresholding, SLA monitoring, and confidence intervals.")
