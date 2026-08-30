
Requirements:
    pip install seaborn matplotlib pandas
"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

OUTPUT_DIR = "seaborn_task_outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ---------------------------------------------------------------------
# Task 1
# Create a Seaborn barplot showing the number of orders per food category
# and save the chart as a PNG file with 300 DPI.
# ---------------------------------------------------------------------
orders_data = pd.DataFrame({
    "Food Category": [
        "Pizza", "Burger", "Biryani", "Momos", "Ice Cream",
        "Pizza", "Burger", "Biryani", "Momos", "Ice Cream",
        "Pizza", "Burger", "Biryani", "Pizza", "Momos",
        "Burger", "Ice Cream", "Biryani", "Pizza", "Momos"
    ]
})

order_counts = (
    orders_data["Food Category"]
    .value_counts()
    .reindex(["Pizza", "Burger", "Biryani", "Momos", "Ice Cream"])
    .reset_index()
)
order_counts.columns = ["Food Category", "Orders"]

plt.figure(figsize=(9, 6))
sns.barplot(
    data=order_counts,
    x="Food Category",
    y="Orders",
    hue="Food Category",
    palette="Set2",
    legend=False
)
plt.title("Number of Orders per Food Category", fontsize=16, fontweight="bold")
plt.xlabel("Food Category")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_DIR, "task1_food_category_orders.png"),
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# ---------------------------------------------------------------------
# Task 2
# Generate a Seaborn line plot of daily step counts for one week and
# export it as an SVG suitable for PowerPoint.
# ---------------------------------------------------------------------
steps_data = pd.DataFrame({
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"],
    "Steps": [7200, 8500, 7900, 10200, 9100, 12000, 6800]
})

plt.figure(figsize=(10, 5.5))
sns.lineplot(
    data=steps_data,
    x="Day",
    y="Steps",
    marker="o",
    linewidth=2.5
)
plt.title("Daily Step Counts - One Week", fontsize=16, fontweight="bold")
plt.xlabel("Day")
plt.ylabel("Steps")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_DIR, "task2_weekly_steps.svg"),
    format="svg",
    bbox_inches="tight"
)
plt.close()


# ---------------------------------------------------------------------
# Task 3
# Customize a Seaborn chart using the darkgrid style and a chosen
# color palette, then save as a high-resolution PNG at 1200 DPI.
# ---------------------------------------------------------------------
sns.set_style("darkgrid")
sns.set_palette("husl")

sales_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 145, 138, 172, 190, 215]
})

plt.figure(figsize=(10, 6))
sns.barplot(
    data=sales_data,
    x="Month",
    y="Sales",
    hue="Month",
    palette="husl",
    legend=False
)
plt.title("Monthly Sales Performance", fontsize=18, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Sales (Units)")
plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_DIR, "task3_darkgrid_highres.png"),
    dpi=1200,
    bbox_inches="tight"
)
plt.close()


# ---------------------------------------------------------------------
# Task 4
# Create a template function that applies a consistent Seaborn style,
# font, and color palette to any chart, then use it for a pie chart
# showing the top 5 most-used apps.
# ---------------------------------------------------------------------
def apply_presentation_theme():
    """Apply a consistent presentation-ready Seaborn theme."""
    sns.set_theme(
        style="whitegrid",
        context="talk",
        font="DejaVu Sans",
        palette="deep"
    )


apply_presentation_theme()

apps_data = pd.DataFrame({
    "App": ["YouTube", "WhatsApp", "Instagram", "Google Chrome", "Spotify"],
    "Usage (hours/week)": [14, 10, 8, 7, 5]
})

plt.figure(figsize=(9, 7))
plt.pie(
    apps_data["Usage (hours/week)"],
    labels=apps_data["App"],
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={"edgecolor": "white", "linewidth": 1.2}
)
plt.title("Top 5 Most-Used Apps", fontsize=18, fontweight="bold")
plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_DIR, "task4_top5_apps_presentation_theme.png"),
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# ---------------------------------------------------------------------
# Task 5
# ChatGPT prompt and received code are preserved below as comments,
# as requested. The code is then adapted to export a Seaborn heatmap
# as an SVG file with dpi=1200.
# ---------------------------------------------------------------------
# ChatGPT prompt:
# "Generate a Python/Seaborn code snippet for exporting a Seaborn
# heatmap as a 1200 DPI SVG file."
#
# ChatGPT-generated code:
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.heatmap(data, annot=True, cmap="viridis")
# plt.savefig("heatmap.svg", format="svg", dpi=1200, bbox_inches="tight")
#
# Adaptation/test:
# I created a 7-day x 5-category dataset and used the same SVG export
# pattern with an explicit 1200 DPI setting.

heatmap_data = pd.DataFrame(
    [
        [12, 18, 10, 14, 8],
        [15, 20, 13, 16, 9],
        [10, 17, 15, 12, 11],
        [18, 22, 14, 19, 12],
        [16, 19, 17, 15, 10],
        [21, 25, 19, 23, 14],
        [14, 16, 12, 18, 9],
    ],
    index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    columns=["Pizza", "Burger", "Biryani", "Momos", "Ice Cream"]
)

plt.figure(figsize=(10, 6.5))
sns.heatmap(
    heatmap_data,
    annot=True,
    fmt="d",
    cmap="viridis",
    linewidths=0.5,
    cbar_kws={"label": "Orders"}
)
plt.title("Weekly Food Category Order Heatmap", fontsize=16, fontweight="bold")
plt.xlabel("Food Category")
plt.ylabel("Day")
plt.tight_layout()
plt.savefig(
    os.path.join(OUTPUT_DIR, "task5_heatmap_1200dpi.svg"),
    format="svg",
    dpi=1200,
    bbox_inches="tight"
)
plt.close()

print("All 5 tasks completed.")
print(f"Files saved in: {os.path.abspath(OUTPUT_DIR)}")
