import matplotlib.pyplot as plt

# Daily listening/viewing hours for the same week
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
spotify_hours = [1.5, 2.0, 1.2, 2.5, 1.8, 3.0, 2.2]
youtube_hours = [1.0, 1.5, 2.0, 1.3, 2.2, 3.4, 2.8]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Spotify plot
axes[0].plot(days, spotify_hours, marker="o", linewidth=2)
axes[0].set_xlabel("Day")
axes[0].set_ylabel("Hours")
axes[0].set_title("Daily Spotify Listening")
axes[0].grid(True, alpha=0.3)

# YouTube plot
axes[1].plot(days, youtube_hours, marker="o", linewidth=2)
axes[1].set_xlabel("Day")
axes[1].set_ylabel("Hours")
axes[1].set_title("Daily YouTube Viewing")
axes[1].grid(True, alpha=0.3)

fig.suptitle("Weekly Entertainment Usage Dashboard", fontsize=14)
fig.tight_layout()
plt.show()
