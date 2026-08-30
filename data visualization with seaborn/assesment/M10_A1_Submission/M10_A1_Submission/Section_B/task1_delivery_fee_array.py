import numpy as np

np.random.seed(42)
distances = np.random.uniform(1.0, 15.0, 25)
fees = 20 + 5 * distances

mask = fees > 60
qualifying_distances = distances[mask]
qualifying_fees = fees[mask]

print("TASK 1: DELIVERY FEE ARRAY CALCULATOR")
print("Orders with delivery fee > Rs 60:")
qualifying_table = np.column_stack((qualifying_distances, qualifying_fees))
print(np.array2string(qualifying_table, formatter={"float_kind": lambda x: f"{x:.2f}"}))

print("\nComplete fee statistics:")
print(f"Minimum: Rs {np.min(fees):.2f}")
print(f"Maximum: Rs {np.max(fees):.2f}")
print(f"Mean: Rs {np.mean(fees):.2f}")
print(f"Standard deviation: Rs {np.std(fees):.2f}")
