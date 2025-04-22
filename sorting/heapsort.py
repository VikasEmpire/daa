import random
import time
import math
import matplotlib.pyplot as plt

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Input sizes
input_sizes = list(range(5000, 200001, 15000))

# Best case: Already sorted (still O(n log n))
def generate_best_case(size):
    return list(range(size))

# Worst case: Reverse-sorted (still O(n log n))
def generate_worst_case(size):
    return list(range(size, 0, -1))

# Average case: Randomly shuffled
def generate_average_case(size):
    arr = list(range(size))
    random.shuffle(arr)
    return arr

# Measure execution time
best_case_times = []
worst_case_times = []
average_case_times = []

for size in input_sizes:
    # Best case
    arr = generate_best_case(size)
    start = time.time()
    heap_sort(arr)
    end = time.time()
    best_case_times.append((end - start) * 1000)

    # Worst case
    arr = generate_worst_case(size)
    start = time.time()
    heap_sort(arr)
    end = time.time()
    worst_case_times.append((end - start) * 1000)

    # Average case
    arr = generate_average_case(size)
    start = time.time()
    heap_sort(arr)
    end = time.time()
    average_case_times.append((end - start) * 1000)

    print(f"Size: {size}, Best: {best_case_times[-1]:.2f} ms, Worst: {worst_case_times[-1]:.2f} ms, Avg: {average_case_times[-1]:.2f} ms")

# Normalize n log n to match scale (for visualization)
n_log_n = [size * math.log2(size) for size in input_sizes]
scale_factor = average_case_times[-1] / n_log_n[-1]
n_log_n_scaled = [x * scale_factor for x in n_log_n]

# Plot all cases + theoretical curve (using line styles)
plt.figure(figsize=(12, 6))
plt.plot(input_sizes, best_case_times, label="Best Case (Sorted)", linestyle="-")  # Solid
plt.plot(input_sizes, average_case_times, label="Average Case (Random)", linestyle="--")  # Dashed
plt.plot(input_sizes, worst_case_times, label="Worst Case (Reverse Sorted)", linestyle=":")  # Dotted
plt.plot(input_sizes, n_log_n_scaled, label="Theoretical O(n log n)", linestyle="-.")  # Dash-dot

plt.title("Heap Sort: Actual vs. Theoretical O(n log n) (Line Styles)")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (ms)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)  # Light grid for clarity
plt.tight_layout()
plt.show()