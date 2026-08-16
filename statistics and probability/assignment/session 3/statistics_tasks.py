# Statistics Tasks - Mean, Median and Mode

# Task 1: Mean of Daily Step Counts
steps = [6500, 7200, 5800, 8000, 7500, 6200, 7000]

mean_steps = sum(steps) / len(steps)

print("TASK 1 - Daily Step Counts")
print("Daily Steps:", steps)
print("Mean (Average) Steps:", round(mean_steps, 2))
print()


# Task 2: Median of Food Delivery Times
delivery_times = [32, 28, 29, 45, 30, 31, 60, 30, 29]

def find_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        middle1 = sorted_data[(n // 2) - 1]
        middle2 = sorted_data[n // 2]
        return (middle1 + middle2) / 2

median_delivery = find_median(delivery_times)

print("TASK 2 - Food Delivery Time")
print("Original Data:", delivery_times)
print("Sorted Data:", sorted(delivery_times))
print("Median Delivery Time:", median_delivery, "minutes")
print()


# Task 3: Mode of YouTube Video Genres
genres = [
    'Music', 'Vlog', 'Music', 'Tech', 'Music', 'Vlog',
    'Tech', 'Music', 'Comedy', 'Vlog', 'Music', 'Comedy'
]

from collections import Counter

genre_count = Counter(genres)
mode_genre = genre_count.most_common(1)[0][0]

print("TASK 3 - YouTube Video Genres")
print("Genre Counts:", genre_count)
print("Most Watched Genre (Mode):", mode_genre)
print()


# Task 4: Mean and Median of UPI Transaction Amounts
transactions = [100, 120, 105, 110, 5000, 115, 108]

mean_transaction = sum(transactions) / len(transactions)
median_transaction = find_median(transactions)

print("TASK 4 - UPI Transaction Amounts")
print("Transactions:", transactions)
print("Mean:", round(mean_transaction, 2))
print("Median:", median_transaction)
print()
print("Explanation:")
print("Median is a better measure of the typical transaction amount.")
print("The ₹5000 value is an outlier that pulls the mean upward to about ₹794,")
print("while the median remains ₹110 and better represents the normal transactions.")
