"""
SESSION 10: Sampling Techniques (Random, Stratified, Systematic, Sample Size Impact)
"""
import numpy as np
import pandas as pd

print("="*60)
print("TASK 1: Random Sampling (20 Users from 200)")
print("="*60)
np.random.seed(42)
all_users = [f"USER_{i:03d}" for i in range(1, 201)]
survey_sample = np.random.choice(all_users, size=20, replace=False)
print(f"Total Users: {len(all_users)}")
print(f"Selected Random Sample (20 Users):")
print(survey_sample.tolist())
print()

print("="*60)
print("TASK 2: Proportional Stratified Sampling (Flipkart Orders by City)")
print("="*60)
np.random.seed(123)
cities = np.random.choice(['Ahmedabad', 'Surat', 'Vadodara'], size=1000, p=[0.50, 0.30, 0.20])
orders_df = pd.DataFrame({'OrderID': range(1, 1001), 'City': cities})
city_counts = orders_df['City'].value_counts()
print("Population Breakdown:")
print(city_counts)

stratified_sample = orders_df.groupby('City', group_keys=False).apply(
    lambda x: x.sample(n=int(round(60 * len(x) / len(orders_df))), random_state=42)
)
print(f"
Stratified Sample (N=60) Breakdown:")
print(stratified_sample['City'].value_counts())
print()

print("="*60)
print("TASK 3: Systematic Sampling Function (Every k-th Item)")
print("="*60)
def systematic_sampling(data_list, step=10):
    start_idx = np.random.randint(0, step) # random start between 0 and step-1
    return data_list[start_idx::step]

zomato_reviews = [f"Review_{i:03d}" for i in range(1, 501)]
sample_reviews = systematic_sampling(zomato_reviews, step=10)
print(f"Total Reviews: {len(zomato_reviews)}")
print(f"Selected Systematic Sample Count: {len(sample_reviews)}")
print(f"First 10 Sampled Elements: {sample_reviews[:10]}
")

print("="*60)
print("TASK 4: Impact of Sample Size on Margin of Error")
print("="*60)
std_est = 8.0 # assume std dev = 8 mins
z_val = 1.96 # for 95% confidence
for n in [50, 200, 500]:
    margin_error = z_val * (std_est / np.sqrt(n))
    print(f"Sample Size n = {n:3d}  -->  Standard Error: {std_est/np.sqrt(n):.3f} mins  -->  Margin of Error (±95%): ±{margin_error:.2f} mins")
print("Conclusion: Increasing sample size from 50 to 500 reduces estimation margin of error by ~68% (from ±2.22 to ±0.70 mins).
")

print("="*60)
print("TASK 5: Stratified Sampling on IPL Fan Dataset")
print("="*60)
np.random.seed(99)
fan_teams = np.random.choice(['CSK', 'MI', 'RCB', 'GT'], size=800, p=[0.35, 0.25, 0.25, 0.15])
fans_df = pd.DataFrame({'FanID': [f"FAN_{i:04d}" for i in range(1, 801)], 'Team': fan_teams})
print("IPL Fan Population:")
print(fans_df['Team'].value_counts())

sample_size_ipl = 40
strat_ipl = fans_df.groupby('Team', group_keys=False).apply(
    lambda x: x.sample(n=int(round(sample_size_ipl * len(x) / len(fans_df))), random_state=42)
)
print(f"
Sampled 40 Fans Across Teams:")
print(strat_ipl['Team'].value_counts())
