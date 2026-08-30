"""
SESSION 17: Introduction to Simple Linear Regression
Tasks 1 - 4 Implementation (Swiggy Ad Spend vs Daily Orders)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def run_session_17_tasks():
    print("=" * 75)
    print("TASK 1: Dependent vs Independent Variables (YouTube Influencer Deals)")
    print("=" * 75)
    print("• Independent Variable (X): Number of Followers (predictor / feature).")
    print("• Dependent Variable (Y): Average Monthly Brand Deals (outcome / target being predicted).")
    print("• Rationale: Brand deals depend on audience size; having more followers causes higher deal acquisition.\n")

    print("=" * 75)
    print("TASK 2: Myntra Ad Spend vs App Downloads Scatter Plot & Best Fit Line")
    print("=" * 75)
    ad_spend_myntra = np.array([1.2, 2.0, 2.8, 3.5, 4.0, 5.2, 6.0, 6.8, 7.5, 8.5]) # Lakhs
    downloads_k     = np.array([15,  22,  28,  34,  40,  50,  58,  65,  72,  84]) # Thousands
    
    # Fit regression line
    model_myntra = LinearRegression()
    model_myntra.fit(ad_spend_myntra.reshape(-1, 1), downloads_k)
    y_pred_myntra = model_myntra.predict(ad_spend_myntra.reshape(-1, 1))

    plt.figure(figsize=(7, 4.5))
    plt.scatter(ad_spend_myntra, downloads_k, color='#2980B9', label='Observed Data', s=60)
    plt.plot(ad_spend_myntra, y_pred_myntra, color='#E74C3C', linewidth=2, label=f'Best Fit Line: Y = {model_myntra.coef_[0]:.2f}X + {model_myntra.intercept_:.2f}')
    plt.title('Myntra Ad Spend (₹ Lakhs) vs App Downloads (in Thousands)', fontsize=12, fontweight='bold')
    plt.xlabel('Ad Spend (₹ Lakhs)')
    plt.ylabel('App Downloads (in Thousands)')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    plt.savefig('session_17_myntra_regression_plot.png', dpi=300)
    plt.close()
    print("Generated and saved 'session_17_myntra_regression_plot.png'.\n")

    print("=" * 75)
    print("TASK 3 & 4: Swiggy Daily Ad Spend vs Daily Orders Regression Model")
    print("=" * 75)
    ad_spend_swiggy = np.array([2.0, 3.0, 4.5, 5.0, 6.5, 7.0, 8.5, 9.0, 10.5, 12.0]).reshape(-1, 1) # ₹ Lakhs
    daily_orders    = np.array([1200, 1550, 1980, 2150, 2600, 2800, 3350, 3500, 3950, 4500])       # Orders
    
    reg_model = LinearRegression()
    reg_model.fit(ad_spend_swiggy, daily_orders)
    predictions = reg_model.predict(ad_spend_swiggy)
    
    slope = reg_model.coef_[0]
    intercept = reg_model.intercept_
    r2 = r2_score(daily_orders, predictions)
    
    print(f"Slope (Coefficient β1): {slope:.2f}")
    print(f"Intercept (β0): {intercept:.2f}")
    print(f"Regression Equation: Daily Orders = {slope:.2f} * (Ad Spend) + {intercept:.2f}")
    print(f"R-squared (R²) Value: {r2:.4f} ({r2*100:.2f}%)")
    print("\nInterpretation:")
    print(f"• Slope meaning: For every additional ₹1 Lakh spent on advertising, Swiggy gains approximately {slope:.0f} additional orders.")
    print(f"• R² Interpretation: The R² value of {r2:.4f} is very close to 1, indicating that {r2*100:.1f}% of the variance in daily orders is explained by ad spend (exceptionally high accuracy).")
    print("=" * 75)

if __name__ == "__main__":
    run_session_17_tasks()
