import numpy as np

def detect_outliers(order_amounts):
    """
    Detect outliers using the IQR method.

    Outlier rule:
    Below Q1 - 1.5*IQR
    or
    Above Q3 + 1.5*IQR
    """
    data = np.array(order_amounts)

    q1 = np.quantile(data, 0.25)
    q3 = np.quantile(data, 0.75)
    iqr = q3 - q1

    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    outliers = data[(data < lower_limit) | (data > upper_limit)]

    return q1, q3, iqr, lower_limit, upper_limit, outliers


# Swiggy order amounts
order_amounts = [
    220, 350, 180, 420, 275,
    310, 260, 390, 450, 290,
    340, 375, 230, 410, 280,
    300, 265, 360, 1250, 320
]

q1, q3, iqr, lower_limit, upper_limit, outliers = detect_outliers(order_amounts)

print("Swiggy Order Amounts:", order_amounts)
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower Bound:", lower_limit)
print("Upper Bound:", upper_limit)
print("Outlier Values:", outliers)

print("\nConclusion:")
if len(outliers) > 0:
    print("The values outside the lower and upper bounds are considered outliers.")
else:
    print("No outliers were detected.")
