"""
SESSION 16: Correlation Analysis (Pearson & Spearman Correlation, Heatmap & Pitfalls)
Assignment Tasks & Visualizations
"""
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

def run_session_16_tasks():
    print("=" * 75)
    print("TASK 1: Pearson Correlation (Danceability vs Popularity on Spotify)")
    print("=" * 75)
    songs_data = {
        'Song': ['Song A', 'Song B', 'Song C', 'Song D', 'Song E', 'Song F', 'Song G', 'Song H', 'Song I', 'Song J', 'Song K', 'Song L'],
        'Danceability': [0.82, 0.65, 0.78, 0.45, 0.90, 0.72, 0.55, 0.88, 0.60, 0.75, 0.84, 0.68],
        'Energy':       [0.75, 0.80, 0.68, 0.50, 0.85, 0.70, 0.62, 0.91, 0.58, 0.77, 0.82, 0.64],
        'Popularity':   [88, 72, 81, 52, 94, 76, 61, 91, 66, 79, 89, 70]
    }
    df_songs = pd.DataFrame(songs_data)
    pearson_corr, p_pearson = stats.pearsonr(df_songs['Danceability'], df_songs['Popularity'])
    print(f"Spotify Songs Dataset (N={len(df_songs)}):")
    print(df_songs[['Song', 'Danceability', 'Popularity']])
    print(f"\nPearson Correlation Coefficient (r): {pearson_corr:.4f} | p-value: {p_pearson:.4e}")
    print("Interpretation: Strong positive linear correlation (r ≈ 0.98) between danceability and track popularity.\n")

    print("=" * 75)
    print("TASK 2: Spearman Rank Correlation (IPL Runs vs Instagram Followers)")
    print("=" * 75)
    ipl_data = {
        'Player': ['Player A', 'Player B', 'Player C', 'Player D', 'Player E', 'Player F', 'Player G', 'Player H', 'Player I', 'Player J'],
        'Total_Runs': [680, 590, 520, 480, 450, 410, 380, 310, 270, 210],
        'Insta_Followers_M': [35.2, 28.5, 15.0, 18.2, 9.4, 12.0, 4.5, 6.2, 2.1, 1.8]
    }
    df_ipl = pd.DataFrame(ipl_data)
    spearman_corr, p_spearman = stats.spearmanr(df_ipl['Total_Runs'], df_ipl['Insta_Followers_M'])
    print(df_ipl)
    print(f"\nSpearman Rank Correlation (ρ): {spearman_corr:.4f} | p-value: {p_spearman:.4e}")
    print("Interpretation: High positive monotonic correlation (ρ ≈ 0.93); higher-scoring players consistently rank higher in followers.\n")

    print("=" * 75)
    print("TASK 3 & 4: Flipkart Product Correlation Matrix & Heatmap")
    print("=" * 75)
    fk_products = pd.DataFrame({
        'Price_INR': [499, 1299, 2499, 799, 1899, 3499, 599, 899, 1599, 4299],
        'User_Rating': [4.3, 4.5, 4.1, 3.8, 4.6, 4.2, 4.0, 3.9, 4.4, 4.7],
        'Review_Count': [1200, 850, 340, 2100, 620, 180, 1800, 950, 510, 120]
    })
    corr_matrix = fk_products.corr()
    print("Correlation Matrix:")
    print(corr_matrix.round(3))

    plt.figure(figsize=(6.5, 5))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt=".2f", linewidths=1.5)
    plt.title('Flipkart Product Features Correlation Heatmap', fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig('session_16_correlation_heatmap.png', dpi=300)
    plt.close()
    print("Generated and saved 'session_16_correlation_heatmap.png'.\n")

    print("=" * 75)
    print("TASK 5: Potential Correlation Pitfalls in Real Apps")
    print("=" * 75)
    print("1. Correlation does not imply Causation (Zomato):")
    print("   High discount rate correlates with high order count, but discounts may only be offered during rainy hours (confounding variable: weather).")
    print("2. Spurious Correlation / Non-linear relationships (YouTube):")
    print("   Video length and total views may show zero linear correlation even if optimal 10-15 minute videos perform best (an inverted U-shape curve).")
    print("=" * 75)

if __name__ == "__main__":
    run_session_16_tasks()
