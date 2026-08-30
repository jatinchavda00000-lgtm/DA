"""
SESSION 8: Discrete Probability Distributions (Bernoulli, Binomial, Poisson)
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

print("="*60)
print("TASK 1: Bernoulli Simulation (Zomato User Login Success)")
print("="*60)
p_login = 0.85
np.random.seed(42)
login_sim = np.random.binomial(n=1, p=p_login, size=20)
print(f"Probability of Success (p) = {p_login}")
print(f"20 Simulated Login Trials (1=Success, 0=Failure):")
print(login_sim.tolist())
print(f"Successes: {sum(login_sim)}/20 ({sum(login_sim)/20*100:.1f}%)
")

print("="*60)
print("TASK 2: Binomial Probability for Paytm UPI Successes")
print("="*60)
n_txns = 5
k_target = 3
p_success = 0.90
prob_k3 = stats.binom.pmf(k=k_target, n=n_txns, p=p_success)
print(f"Attempts (n) = {n_txns}, Successes (k) = {k_target}, Success Rate (p) = {p_success}")
print(f"P(X = 3) = {prob_k3:.4f} ({prob_k3*100:.2f}%)
")

print("="*60)
print("TASK 3: Poisson Probability for Spotify Playlist Creation")
print("="*60)
lambda_spotify = 4 # avg per min
k_spotify = 6
prob_spotify_6 = stats.poisson.pmf(k=k_spotify, mu=lambda_spotify)
print(f"Mean rate (λ) = {lambda_spotify} playlists/min, Target (k) = {k_spotify}")
print(f"P(X = 6) = {prob_spotify_6:.4f} ({prob_spotify_6*100:.2f}%)
")

print("="*60)
print("TASK 4: Simulating & Plotting Flipkart Reviews per Hour (Poisson)")
print("="*60)
lambda_flipkart = 10
hours = 12
np.random.seed(101)
simulated_reviews = np.random.poisson(lam=lambda_flipkart, size=hours)
print(f"Simulated Hourly Reviews for 12 Hours: {simulated_reviews.tolist()}")

plt.figure(figsize=(9, 4.5))
plt.bar(range(1, hours+1), simulated_reviews, color='#2874A6', edgecolor='black', alpha=0.85)
plt.axhline(lambda_flipkart, color='red', linestyle='--', linewidth=1.5, label=f'Expected λ = {lambda_flipkart}')
plt.title('Flipkart Hourly Product Reviews (12-Hour Poisson Simulation)', fontsize=12, fontweight='bold')
plt.xlabel('Hour Index', fontsize=10)
plt.ylabel('Number of Reviews Received', fontsize=10)
plt.xticks(range(1, hours+1))
plt.legend()
plt.grid(axis='y', linestyle=':', alpha=0.6)
plt.savefig('session_08_flipkart_poisson_reviews.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved Poisson simulation plot as 'session_08_flipkart_poisson_reviews.png'.
")

print("="*60)
print("TASK 5: Real-World Analytics Distribution Selection")
print("="*60)
print("Selected Distribution: Poisson Distribution")
print("Use Case (IRCTC): Modeling the count of tatkal ticket booking queries received per second during peak 10:00 AM rush.")
print("Rationale: The event count is discrete, independent, occurs within a fixed time window, and the underlying rate is high without a predefined ceiling.")
