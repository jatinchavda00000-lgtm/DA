import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

OUTPUT_DIR = "."


def build_dataset(seed=2026, n=250):
    np.random.seed(seed)
    restaurants = np.array(["Spice Route", "Urban Bites", "Dragon Bowl", "Pizza Hub", "Sweet Treats"])
    cuisines = np.array(["Indian", "Chinese", "Fast Food"])
    df = pd.DataFrame({
        "restaurant_name": np.random.choice(restaurants, n),
        "cuisine_type": np.random.choice(cuisines, n),
        "order_value": np.random.uniform(100, 900, n),
        "distance_km": np.random.uniform(1, 20, n),
        "delivery_time_mins": np.random.normal(30, 7, n),
        "rating": np.random.uniform(1, 5, n),
        "discount_pct": np.random.uniform(0, 30, n),
        "driver_experience_years": np.random.uniform(0.5, 12, n),
    })
    # Add some nulls intentionally so the startup cleaning requirement is exercised.
    for col in ["order_value", "delivery_time_mins", "rating"]:
        idx = np.random.choice(df.index, size=8, replace=False)
        df.loc[idx, col] = np.nan

    numeric_cols = df.select_dtypes(include=np.number).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())
    return df


def summary_statistics(df):
    stats = df[["order_value", "distance_km", "delivery_time_mins", "rating"]].describe().T
    print("\nSUMMARY STATISTICS")
    print(stats[["mean", "std", "min", "max"]].round(2).to_string())
    print(f"Overall mean order value (NumPy): Rs {np.mean(df['order_value']):.2f}")


def distribution_analysis(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["delivery_time_mins"], bins=15)
    ax.set_title("Delivery Time Distribution")
    ax.set_xlabel("Delivery Time (mins)")
    ax.set_ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("distribution_analysis.png", dpi=180, bbox_inches="tight")
    plt.close(fig)
    print("Saved distribution_analysis.png")


def correlation_heatmap(df):
    corr = df.select_dtypes(include=np.number).corr()
    plt.figure(figsize=(9, 7))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0, vmin=-1, vmax=1)
    plt.title("Numeric Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("correlation_heatmap_capstone.png", dpi=180, bbox_inches="tight")
    plt.close()
    print("Saved correlation_heatmap_capstone.png")


def restaurant_performance_report(df):
    report = (
        df.groupby("restaurant_name")
          .agg(mean_order_value=("order_value", "mean"),
               mean_delivery_time=("delivery_time_mins", "mean"),
               mean_rating=("rating", "mean"),
               order_count=("order_value", "size"))
          .sort_values("mean_rating", ascending=False)
    )
    print("\nRESTAURANT PERFORMANCE REPORT")
    print(report.round(2).to_string())


def final_report(df):
    report = (
        df.groupby("restaurant_name")["rating"]
          .mean()
          .sort_values(ascending=False)
          .head(3)
    )
    numeric_df = df.select_dtypes(include=np.number)
    corr = numeric_df.corr()
    pairs = corr.where(~np.eye(len(corr), dtype=bool)).stack()
    top_pair = pairs.abs().sort_values(ascending=False).index[0]
    top_value = corr.loc[top_pair[0], top_pair[1]]

    print("\nFINAL SUMMARY REPORT")
    print("Top 3 restaurants by mean rating:")
    for restaurant, rating in report.items():
        print(f"- {restaurant}: {rating:.2f}")
    print(f"Highest absolute Pearson correlation pair: {top_pair[0]} vs {top_pair[1]} (r={top_value:.3f})")
    print(f"Overall delivery-time mean: {np.mean(df['delivery_time_mins']):.2f} minutes")
    print(f"Overall delivery-time standard deviation: {np.std(df['delivery_time_mins']):.2f} minutes")


def main():
    df = build_dataset()
    print("FOOD DELIVERY ANALYTICS CONSOLE")
    print(f"Dataset ready: {len(df)} rows | numeric nulls filled before analysis")

    while True:
        print("\n1. Summary Statistics")
        print("2. Distribution Analysis")
        print("3. Correlation Heatmap")
        print("4. Restaurant Performance Report")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            summary_statistics(df)
        elif choice == "2":
            distribution_analysis(df)
        elif choice == "3":
            correlation_heatmap(df)
        elif choice == "4":
            restaurant_performance_report(df)
        elif choice == "5":
            final_report(df)
            print("\nProgram exited successfully.")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
