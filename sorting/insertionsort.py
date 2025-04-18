
import matplotlib.pyplot as plt
import random
import time
import math

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

input_sizes = list(range(100, 10001, 1000))
execution_times = []

for size in input_sizes:
    arr = [random.randint(0, size) for i in range(size)]
    start_time = time.perf_counter()
    insertion_sort(arr)
    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000
    execution_times.append(elapsed_time)
    print(f"Size: {size}, Time: {elapsed_time:.4f} ms")

n_squared_values = [n**2 / 20000 for n in input_sizes]

plt.figure(figsize=(10, 6))
plt.plot([0, 10000], [0, 700], color='red', linestyle='-', linewidth=2, label='Linear O(n)')
plt.plot(input_sizes, execution_times, linestyle='-', color='blue', label='Insertion Sort O(n²)')
plt.plot(input_sizes, n_squared_values, linestyle=':', color='purple', label='O(n²) (scaled)')
plt.title("Insertion Sort Time Complexity Analysis")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (ms)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
