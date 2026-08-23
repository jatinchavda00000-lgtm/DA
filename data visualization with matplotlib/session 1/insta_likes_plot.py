import matplotlib.pyplot as plt

# Made-up likes data for the last 10 Instagram posts
posts = [f"Post {i}" for i in range(1, 11)]
likes = [420, 510, 680, 590, 760, 840, 710, 930, 880, 1020]

plt.figure(figsize=(9, 5))
plt.plot(posts, likes, marker="o", linewidth=2)

plt.xlabel("Instagram Post")
plt.ylabel("Number of Likes")
plt.title("Instagram Likes - Last 10 Posts")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
