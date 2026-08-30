"""
SESSION 15: ANOVA (Analysis of Variance)
Tasks 1 - 5 Implementation & Purchase Data Analysis
"""
import numpy as np
import pandas as pd
from scipy import stats

def run_session_15_tasks():
    print("=" * 75)
    print("TASK 1 & 2: One-Way ANOVA on Customer Purchase Values across Age Groups")
    print("=" * 75)
    # Create dataset of 15 samples across 3 age groups
    data_dict = {
        'customer_id': [f"CUST_{i:02d}" for i in range(1, 16)],
        'age_group': ['18-25']*5 + ['26-35']*5 + ['36-50']*5,
        'purchase_value': [450, 520, 480, 510, 490,   850, 920, 780, 890, 810,   1200, 1150, 1300, 1250, 1180]
    }
    df_purchases = pd.DataFrame(data_dict)
    df_purchases.to_csv('purchase_data.csv', index=False)
    print("Saved purchase_data.csv. First 5 rows:")
    print(df_purchases.head())
    
    g1 = df_purchases[df_purchases['age_group'] == '18-25']['purchase_value']
    g2 = df_purchases[df_purchases['age_group'] == '26-35']['purchase_value']
    g3 = df_purchases[df_purchases['age_group'] == '36-50']['purchase_value']
    
    f_stat, p_val = stats.f_oneway(g1, g2, g3)
    print(f"\nGroup Means: 18-25: ₹{g1.mean():.2f} | 26-35: ₹{g2.mean():.2f} | 36-50: ₹{g3.mean():.2f}")
    print(f"ANOVA F-statistic: {f_stat:.4f} | p-value: {p_val:.4e}\n")

    print("=" * 75)
    print("TASK 3: Analytical Conclusion")
    print("=" * 75)
    print("Interpretation:")
    print("Because p-value < 0.001 (far below 0.05), we reject the null hypothesis.")
    print("There is a highly statistically significant difference in average purchase values across age groups,")
    print("with purchase power increasing consistently from younger to older cohorts.\n")

    print("=" * 75)
    print("TASK 4: Between-Group vs Within-Group Variance Calculation")
    print("=" * 75)
    overall_mean = df_purchases['purchase_value'].mean()
    # Between-group sum of squares (SSB)
    ssb = sum(len(g) * (g.mean() - overall_mean)**2 for g in [g1, g2, g3])
    df_between = 3 - 1 # k - 1 = 2
    msb = ssb / df_between
    
    # Within-group sum of squares (SSW)
    ssw = sum(sum((g - g.mean())**2) for g in [g1, g2, g3])
    df_within = len(df_purchases) - 3 # N - k = 12
    msw = ssw / df_within
    
    print(f"Between-Group Mean Square (MSB): {msb:.2f} (Variance between age category averages)")
    print(f"Within-Group Mean Square (MSW): {msw:.2f} (Natural variation among customers in same age group)")
    print(f"Computed F = MSB / MSW = {msb/msw:.4f}\n")

    print("=" * 75)
    print("TASK 5: Zomato Customer Segments (Students, Professionals, Retirees)")
    print("=" * 75)
    students = [220, 250, 180, 290, 210]
    professionals = [550, 620, 580, 670, 530]
    retirees = [380, 420, 390, 450, 360]
    f_zom, p_zom = stats.f_oneway(students, professionals, retirees)
    print(f"Segment Means: Students: ₹{np.mean(students):.1f} | Professionals: ₹{np.mean(professionals):.1f} | Retirees: ₹{np.mean(retirees):.1f}")
    print(f"Zomato F-statistic: {f_zom:.4f} | p-value: {p_zom:.4e}")
    print("Result: Reject H0 — Ordering spend varies significantly across customer lifestyle tiers.")
    print("=" * 75)

if __name__ == "__main__":
    run_session_15_tasks()
