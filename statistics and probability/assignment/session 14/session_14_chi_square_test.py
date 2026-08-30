"""
SESSION 14: Chi-Square Test (Goodness of Fit & Test of Independence)
Assignment Tasks & Python Scipy Implementation
"""
import numpy as np
import pandas as pd
from scipy import stats

def run_session_14_tasks():
    print("=" * 75)
    print("TASK 1 & 3: Contingency Table & Chi-Square Independence Test (Food App vs Payment)")
    print("=" * 75)
    # Contingency Table: Apps (Zomato, Swiggy, Uber Eats) x Payment (Paytm, PhonePe, Credit Card)
    data = np.array([
        [12, 18, 10],  # Zomato
        [15, 20, 8],   # Swiggy
        [5,  8,  12]   # Uber Eats
    ])
    df_ct = pd.DataFrame(data, index=['Zomato', 'Swiggy', 'Uber Eats'], columns=['Paytm', 'PhonePe', 'Credit Card'])
    print("Observed Contingency Table:")
    print(df_ct)
    
    chi2_stat, p_val, dof, expected = stats.chi2_contingency(df_ct)
    print(f"\nChi-Square Statistic: {chi2_stat:.4f} | Degrees of Freedom: {dof} | p-value: {p_val:.4f}")
    print("Expected Frequencies:")
    print(pd.DataFrame(expected, index=df_ct.index, columns=df_ct.columns).round(2))
    if p_val < 0.05:
        print("Conclusion: Reject H0 — Significant dependency between Food App and Payment Method.\n")
    else:
        print("Conclusion: Fail to Reject H0 — Food App and Payment Method are independent (p >= 0.05).\n")

    print("=" * 75)
    print("TASK 2: Expected Counts for Music Streaming Preference (Gender vs Platform)")
    print("=" * 75)
    # Males: [12 Spotify, 8 Gaana, 10 YT Music] -> Total = 30
    # Females: [18 Spotify, 7 Gaana, 15 YT Music] -> Total = 40
    music_observed = np.array([
        [12, 8, 10],
        [18, 7, 15]
    ])
    row_totals = music_observed.sum(axis=1) # [30, 40]
    col_totals = music_observed.sum(axis=0) # [30, 15, 25]
    grand_total = music_observed.sum()      # 70
    
    # Expected formula = (Row Total * Col Total) / Grand Total
    music_expected = np.outer(row_totals, col_totals) / grand_total
    df_exp = pd.DataFrame(music_expected, index=['Males', 'Females'], columns=['Spotify', 'Gaana', 'YouTube Music'])
    print("Expected Counts Table (Row Total * Col Total / Grand Total):")
    print(df_exp.round(2))
    print()

    print("=" * 75)
    print("TASK 4: Chi-Square Goodness of Fit Test (Flipkart Product Launch)")
    print("=" * 75)
    # Claim: 70% prefer new product, 30% do not. Total N = 30
    observed_fk = np.array([18, 12]) # 18 prefer, 12 do not
    expected_fk = np.array([0.70 * 30, 0.30 * 30]) # [21, 9]
    chi2_gof, p_gof = stats.chisquare(f_obs=observed_fk, f_exp=expected_fk)
    
    print(f"Observed: Prefer={observed_fk[0]}, Do Not Prefer={observed_fk[1]}")
    print(f"Expected (Claimed 70%/30%): Prefer={expected_fk[0]}, Do Not Prefer={expected_fk[1]}")
    print(f"Chi-Square Statistic: {chi2_gof:.4f} | p-value: {p_gof:.4f}")
    if p_gof < 0.05:
        print("Conclusion: Reject H0 — The observed sample deviates significantly from the 70% claim.")
    else:
        print("Conclusion: Fail to Reject H0 — The sample fits the company's 70% preference claim (p >= 0.05).")
    print("=" * 75)

if __name__ == "__main__":
    run_session_14_tasks()
