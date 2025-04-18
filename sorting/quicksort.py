import matplotlib.pyplot as plt
import random
import time
import statistics
import math

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x < pivot]
    right = [x for x in arr[:-1] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

# Input sizes
input_sizes = list(range(5000, 200001, 15000))
execution_times = []

# Measure execution time
for size in input_sizes:
    arr = [random.randint(0, size) for _ in range(size)]
    start = time.time()
    quicksort(arr)
    end = time.time()
    elapsed_time = (end - start) * 1000  # in milliseconds
    execution_times.append(elapsed_time)
    print(f"Size: {size}, Time: {elapsed_time:.4f} ms")

# Theoretical growth
nlogn_growth = [n * math.log2(n) for n in input_sizes]
n_squared_growth = [n ** 2 for n in input_sizes]

# Normalize all
max_time = max(execution_times)
max_nlogn = max(nlogn_growth)
max_n2 = max(n_squared_growth)

normalized_time = [t / max_time for t in execution_times]
normalized_nlogn = [g / max_nlogn for g in nlogn_growth]
normalized_n2 = [g / max_n2 for g in n_squared_growth]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, normalized_time, label="Quicksort Timing (normalized)", color="blue")
plt.plot(input_sizes, normalized_nlogn, label="O(n log n) (normalized)", color="green", linestyle="--")
plt.plot(input_sizes, normalized_n2, label="O(n²) (normalized)", color="red", linestyle=":")

plt.title("Quicksort Growth Comparison with O(n log n) and O(n²)")
plt.xlabel("Input Size (n)")
plt.ylabel("Normalized Values")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

