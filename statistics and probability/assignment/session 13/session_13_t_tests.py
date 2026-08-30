"""
SESSION 13: t-tests (One-Sample, Independent Two-Sample, Paired t-test)
Assignment Tasks & Python Scipy Implementation
"""
import numpy as np
from scipy import stats

def run_session_13_tasks():
    print("=" * 75)
    print("TASK 1: One-Sample t-test for Zomato Delivery Times")
    print("=" * 75)
    # H0: μ = 30 mins vs H1: μ != 30 mins
    sample_data = np.array([28, 32, 27, 35, 29, 31, 30, 33, 26, 34])
    mu_claimed = 30
    t_stat, p_val = stats.ttest_1samp(sample_data, mu_claimed)
    print(f"Sample Data: {sample_data.tolist()}")
    print(f"Sample Mean: {np.mean(sample_data):.2f} mins | Target μ: {mu_claimed} mins")
    print(f"One-Sample t-statistic: {t_stat:.4f} | p-value: {p_val:.4f}")
    if p_val < 0.05:
        print("Conclusion: Reject H0 — Delivery times differ significantly from 30 mins.")
    else:
        print("Conclusion: Fail to Reject H0 — No significant difference from 30 mins (p >= 0.05).\n")

    print("=" * 75)
    print("TASK 2: Independent Two-Sample t-test for Fitness App Step Counts")
    print("=" * 75)
    np.random.seed(42)
    steps_before = np.random.normal(loc=6200, scale=800, size=15)
    steps_after = np.random.normal(loc=7400, scale=850, size=15)
    t_stat_ind, p_val_ind = stats.ttest_ind(steps_after, steps_before)
    print(f"Mean Steps Before: {np.mean(steps_before):.1f} | Mean Steps After: {np.mean(steps_after):.1f}")
    print(f"Independent t-statistic: {t_stat_ind:.4f} | p-value: {p_val_ind:.4e}")
    print(f"Conclusion: {'Statistically Significant Increase (p < 0.05)' if p_val_ind < 0.05 else 'No Significant Difference'}\n")

    print("=" * 75)
    print("TASK 3: Paired t-test for Focus Mode Screen Time (Same Users)")
    print("=" * 75)
    screen_before = np.array([5.5, 6.2, 4.8, 7.0, 5.0, 6.5, 5.8, 6.0, 7.2, 5.4])
    screen_after  = np.array([4.2, 4.8, 4.1, 5.2, 4.0, 5.1, 4.5, 4.9, 5.5, 4.3])
    t_stat_pair, p_val_pair = stats.ttest_rel(screen_after, screen_before)
    print(f"Mean Screen Time Before: {np.mean(screen_before):.2f} hrs | After: {np.mean(screen_after):.2f} hrs")
    print(f"Paired t-statistic: {t_stat_pair:.4f} | p-value: {p_val_pair:.4e}")
    print("Conclusion: Focus Mode significantly reduced daily screen time (p < 0.001).\n")

    print("=" * 75)
    print("TASK 4: Test Selection Rationale — Zomato vs Swiggy Ratings")
    print("=" * 75)
    print("Chosen Test: Independent Two-Sample t-test (stats.ttest_ind)")
    print("Rationale: The two food delivery apps represent two completely independent customer groups rating different platforms.\n")

    print("=" * 75)
    print("TASK 5: PhonePe Daily UPI Transactions One-Sample t-test")
    print("=" * 75)
    upi_user_txns = np.array([4.5, 5.2, 6.0, 3.8, 5.5, 4.9, 6.2, 5.0, 4.8, 5.8, 6.5, 5.1])
    claimed_upi_avg = 4.0
    t_phonepe, p_phonepe = stats.ttest_1samp(upi_user_txns, claimed_upi_avg)
    print(f"User Transactions/day: {upi_user_txns.tolist()}")
    print(f"Sample Mean: {np.mean(upi_user_txns):.2f} | Claimed μ: {claimed_upi_avg}")
    print(f"t-statistic: {t_phonepe:.4f} | p-value: {p_phonepe:.4e}")
    print("Result: Reject H0; actual average daily transactions per user is significantly higher than 4.0.")
    print("=" * 75)

if __name__ == "__main__":
    run_session_13_tasks()
