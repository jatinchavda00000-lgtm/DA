#!/usr/bin/env python
# coding: utf-8

# 
# # Seaborn Visualization Tasks
# 
# This notebook completes all 5 requested Seaborn tasks using simulated/example data. Each task includes the code and a short observation where requested.
# 
# **Libraries:** `pandas`, `matplotlib`, `seaborn`
# 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
sns.set_theme()  # start from Seaborn defaults
print("Seaborn version:", sns.__version__)


# 
# ## Task 1 — Spotify songs streamed per day with `poster` context
# 
# We first show the default context, then use `sns.set(context='poster')` to make plot elements larger for a poster-style display.
# 

# In[2]:


# Example Spotify-style daily stream counts
spotify = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Songs Streamed": [82, 95, 76, 110, 135, 160, 142]
})

# Default context for comparison
sns.set_theme(context="notebook", style="whitegrid", palette="deep")
plt.figure(figsize=(9, 5))
sns.barplot(data=spotify, x="Day", y="Songs Streamed", color="steelblue")
plt.title("Spotify Songs Streamed Per Day — Default Context")
plt.tight_layout()
plt.show()

# Poster context requested in the task
sns.set(context="poster", style="whitegrid", palette="deep")
plt.figure(figsize=(9, 5))
sns.barplot(data=spotify, x="Day", y="Songs Streamed", color="steelblue")
plt.title("Spotify Songs Streamed Per Day — Poster Context")
plt.tight_layout()
plt.show()


# 
# **Observation:** With the `poster` context, titles, tick labels, axis labels, and other plot elements become noticeably larger and easier to read from a distance. The chart therefore feels more suitable for a poster or large-screen presentation than the default context.
# 

# 
# ## Task 2 — Zomato-style cuisine order distribution with the `colorblind` palette
# 
# A countplot is used to show how many food orders belong to each cuisine type.
# 

# In[3]:


food_orders = pd.DataFrame({
    "Cuisine": (
        ["Indian"] * 12
        + ["Chinese"] * 8
        + ["Italian"] * 6
        + ["Mexican"] * 5
        + ["Thai"] * 4
    )
})

sns.set_theme(context="notebook", style="whitegrid")
plt.figure(figsize=(9, 5))
sns.countplot(
    data=food_orders,
    x="Cuisine",
    hue="Cuisine",
    palette="colorblind",
    legend=False,
    order=["Indian", "Chinese", "Italian", "Mexican", "Thai"]
)
plt.title("Food Orders by Cuisine Type")
plt.xlabel("Cuisine Type")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.show()


# 
# **Result:** The `colorblind` palette provides clearly distinguishable colors designed to remain easier to differentiate for viewers with common forms of color-vision deficiency.
# 

# 
# ## Task 3 — Daily step counts for two weeks with `muted` palette and `notebook` context
# 

# In[4]:


dates = pd.date_range("2026-08-01", periods=14, freq="D")
steps = np.array([7200, 8400, 6100, 9300, 10100, 8800, 7600,
                  8200, 9700, 11200, 10800, 8900, 10400, 11800])
steps_df = pd.DataFrame({"Date": dates, "Steps": steps})

sns.set_theme(context="notebook", style="whitegrid", palette="muted")
plt.figure(figsize=(11, 5))
sns.lineplot(data=steps_df, x="Date", y="Steps", marker="o", linewidth=2.5)
plt.title("Daily Step Counts — Two Weeks")
plt.xlabel("Date")
plt.ylabel("Steps")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 
# **Result:** The `muted` palette gives the line a softer, less aggressive appearance, while the `notebook` context keeps text and markers at a balanced size for a clean presentation on a notebook screen.
# 

# 
# ## Task 4 — Refactor a Seaborn plot: `deep` → `colorblind` and `talk` → `poster`
# 
# The same dataset is plotted twice so the visual changes are easy to compare.
# 

# In[5]:


monthly_listens = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Streams": [420, 510, 495, 620, 710, 680]
})

# Existing version: deep palette + talk context
sns.set(palette="deep", context="talk", style="whitegrid")
plt.figure(figsize=(10, 5))
sns.barplot(data=monthly_listens, x="Month", y="Streams", color=sns.color_palette()[0], errorbar=None)
plt.title("Monthly Streams — Original (deep + talk)")
plt.xlabel("Month")
plt.ylabel("Streams (thousands)")
plt.tight_layout()
plt.show()

# Refactored version: colorblind palette + poster context
sns.set(palette="colorblind", context="poster", style="whitegrid")
plt.figure(figsize=(10, 5))
sns.barplot(data=monthly_listens, x="Month", y="Streams", color=sns.color_palette("colorblind")[0], errorbar=None)
plt.title("Monthly Streams — Refactored (colorblind + poster)")
plt.xlabel("Month")
plt.ylabel("Streams (thousands)")
plt.tight_layout()
plt.show()


# 
# ### Visual differences observed
# 
# - **`deep` → `colorblind`:** the color set becomes more accessibility-conscious, with hues chosen to improve differentiation for viewers with common color-vision deficiencies.
# - **`talk` → `poster`:** typography and other visual elements become larger and more prominent.
# - **Overall:** the refactored chart is easier to read from a distance and uses a palette that is generally more accessible.
# 

# 
# ## Task 5 — Flipkart-style sales dashboard theme
# 
# We use `sns.set()` with a `deep` palette, `talk` context, a larger font scale, and a white-grid style. The barplot shows sales across five product categories.
# 

# In[6]:


# Flipkart-style dashboard example data (illustrative)
sales = pd.DataFrame({
    "Category": ["Mobiles", "Electronics", "Fashion", "Home", "Grocery"],
    "Sales (₹ lakh)": [185, 150, 125, 92, 78]
})

# Requested custom theme
sns.set(
    palette="deep",
    context="talk",
    font_scale=1.05,
    style="whitegrid"
)

plt.figure(figsize=(11, 6))
ax = sns.barplot(
    data=sales,
    x="Category",
    y="Sales (₹ lakh)",
    hue="Category",
    legend=False,
    errorbar=None
)

plt.title("Flipkart-Style Product Category Sales")
plt.xlabel("Product Category")
plt.ylabel("Sales (₹ lakh)")
plt.xticks(rotation=0)

# Add data labels for a dashboard-like presentation
for container in ax.containers:
    ax.bar_label(container, fmt="%.0f", padding=3)

plt.tight_layout()
plt.show()


