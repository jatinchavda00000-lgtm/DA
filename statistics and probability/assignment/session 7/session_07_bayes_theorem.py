"""
SESSION 7: Conditional Probability & Bayes' Theorem
"""
print("="*60)
print("TASK 1: E-Commerce Accessories & Phone Conditional Probability")
print("="*60)
total_users = 500
n_acc = 120
n_phone = 80
n_both = 50
p_phone_given_acc = n_both / n_acc
print(f"Total Users: {total_users} | Accessories (B): {n_acc} | Both (A ∩ B): {n_both}")
print(f"P(Phone | Accessories) = N(Both) / N(Accessories) = {n_both} / {n_acc} = {p_phone_given_acc:.4f} ({p_phone_given_acc*100:.2f}%)
")

print("="*60)
print("TASK 2: Flipkart Headphones & Smartphone Conditional Probability")
print("="*60)
p_headphones = 0.30
p_phone_and_headphone = 0.30 * 0.40 # 0.12
p_phone_given_headphone = p_phone_and_headphone / p_headphones
print(f"P(Headphones) = {p_headphones:.2f}")
print(f"P(Phone | Headphones) = {p_phone_given_headphone:.2f} (40.0%)
")

print("="*60)
print("TASK 3: Bayes Churn Probability Function")
print("="*60)
def bayes_churn_probability(prior_churn, prob_email_given_churn, prob_email):
    """
    Computes P(Churn | Email) using Bayes' Theorem:
    P(Churn | Email) = [P(Email | Churn) * P(Churn)] / P(Email)
    """
    posterior = (prob_email_given_churn * prior_churn) / prob_email
    return posterior

prior_churn = 0.15
prob_email_given_churn = 0.60
prob_email = 0.25
churn_post = bayes_churn_probability(prior_churn, prob_email_given_churn, prob_email)
print(f"Prior P(Churn) = {prior_churn}")
print(f"P(Email | Churn) = {prob_email_given_churn}")
print(f"P(Email) = {prob_email}")
print(f"Calculated Posterior P(Churn | Email) = {churn_post:.4f} ({churn_post*100:.2f}%)
")

print("="*60)
print("TASK 4: Digital Wallet Fraud Detection via Bayes' Theorem")
print("="*60)
p_fraud = 0.02
p_normal = 0.98
p_alert_given_fraud = 0.90
p_alert_given_normal = 0.05
# Total P(Alert)
p_alert = (p_alert_given_fraud * p_fraud) + (p_alert_given_normal * p_normal)
p_fraud_given_alert = (p_alert_given_fraud * p_fraud) / p_alert
print(f"P(Fraud) = {p_fraud} | P(Normal) = {p_normal}")
print(f"P(Alert | Fraud) = {p_alert_given_fraud} | P(Alert | Normal) = {p_alert_given_normal}")
print(f"Total P(Alert) = {p_alert:.4f}")
print(f"P(Fraud | Alert) = {p_fraud_given_alert:.4f} ({p_fraud_given_alert*100:.2f}%)")
print("Insight: Even with 90% accuracy, because fraud is rare (base rate 2%), flagged alerts are truly fraudulent ~26.87% of the time due to false positives from normal transactions.
")

print("="*60)
print("TASK 5: Real-World Food Delivery AI Recommendation Context")
print("="*60)
print("AI Scenario: Predicting P(Customer Orders Dessert | Late Night + Biryani Ordered)")
print("Analysis: Bayes' Theorem allows dynamic belief updates—integrating prior customer dietary habits with contextual real-time signals (time of day, weather, order basket) to boost cross-sell conversion.")
