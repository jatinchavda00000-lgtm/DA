"""
SESSION 12: Hypothesis Testing Concepts
Tasks 1 - 4 Comprehensive Solutions & Rationale
"""

def run_session_12_tasks():
    print("=" * 75)
    print("TASK 1: State Hypotheses for Zomato Cashback Offer")
    print("=" * 75)
    print("Null Hypothesis (H0): The new cashback offer has NO effect on the average number of daily orders.")
    print("                      H0: μ_after <= μ_before (or μ_after = μ_before)")
    print("Alternative Hypothesis (H1): The new cashback offer has INCREASED the average number of daily orders.")
    print("                      H1: μ_after > μ_before (Right-tailed test)\n")

    print("=" * 75)
    print("TASK 2: Type I vs Type II Error in Music Streaming App")
    print("=" * 75)
    print("Scenario: Claim that new playlist recommendation increases listening time from 40 to 45 mins.")
    print("Answer:")
    print("If you wrongly conclude the algorithm works when it actually doesn't, this is a TYPE I ERROR (False Positive),")
    print("which occurs when you reject the true null hypothesis (H0).\n")

    print("=" * 75)
    print("TASK 3: Flipkart A/B Test p-value Decision (p = 0.03 at 95% Confidence)")
    print("=" * 75)
    print("Given:")
    print("• Significance Level (α) = 1 - 0.95 = 0.05 (5%)")
    print("• Obtained p-value = 0.03 (3%)")
    print("Decision:")
    print("Since p-value (0.03) < α (0.05), we REJECT the null hypothesis (H0).")
    print("Business Meaning: There is statistically significant evidence at the 95% confidence level")
    print("that the new discount banner genuinely increases purchases on Flipkart, not just by random chance.\n")

    print("=" * 75)
    print("TASK 4: 99% Confidence Level for Cricket App Push Notifications")
    print("=" * 75)
    print("Answer:")
    print("• A 99% confidence level means you set α = 0.01 (1%), requiring a 99% certainty threshold before claiming success.")
    print("• Impact on Decision: This makes the threshold to adopt the feature much stricter, minimizing the risk of a Type I error")
    print("  (annoying users with unwanted notifications when there is no real engagement gain).")
    print("  The team will only accept the feature if the empirical p-value is below 0.01.")
    print("=" * 75)

if __name__ == "__main__":
    run_session_12_tasks()
