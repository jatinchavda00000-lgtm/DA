import matplotlib.pyplot as plt

# Daily usage data for one week
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
spotify_hours = [1.5, 2.0, 1.2, 2.5, 1.8, 3.0, 2.2]
youtube_hours = [1.0, 1.5, 2.0, 1.3, 2.2, 3.4, 2.8]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Spotify Analytics
axes[0].plot(days, spotify_hours, marker="o", linewidth=2)
axes[0].set_xlabel("Day")
axes[0].set_ylabel("Listening Hours")
axes[0].set_title("Spotify Insights")
axes[0].grid(True, alpha=0.3)

# YouTube Analytics
axes[1].plot(days, youtube_hours, marker="o", linewidth=2)
axes[1].set_xlabel("Day")
axes[1].set_ylabel("Viewing Hours")
axes[1].set_title("YouTube Insights")
axes[1].grid(True, alpha=0.3)

fig.suptitle("Weekly Media Analytics Dashboard", fontsize=15)
fig.tight_layout()
plt.show()
