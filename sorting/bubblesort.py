import matplotlib.pyplot as plt
import random
import time
import math

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

input_sizes = list(range(100, 10001, 1000))
execution_times = []

for size in input_sizes:
    arr = [random.randint(0, size) for i in range(size)]
    start_time = time.perf_counter()
    bubble_sort(arr)
    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000
    execution_times.append(elapsed_time)
    print(f"Size: {size}, Time: {elapsed_time:.4f} ms")

n_squared_values = [n**2 / 20000 for n in input_sizes]

plt.figure(figsize=(10, 6))
plt.plot([0, 10000], [0, 700], color='red', linestyle='-', linewidth=2, label='Linear O(n)')
plt.plot(input_sizes, execution_times, linestyle='-', color='blue', label='Bubble Sort O(n²)')
plt.plot(input_sizes, n_squared_values, linestyle=':', color='purple', label='O(n²) (scaled)')
plt.title("Bubble Sort Time Complexity Analysis")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (ms)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
