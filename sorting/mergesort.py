
import matplotlib.pyplot as plt
import random
import time
import math

def merge(arr, start, middle, end):
    temp = [0] * (end - start + 1)
    left = start
    right = middle + 1
    temp_index = 0

    while left <= middle and right <= end:
        if arr[left] < arr[right]:
            temp[temp_index] = arr[left]
            left += 1
        else:
            temp[temp_index] = arr[right]
            right += 1
        temp_index += 1

    while left <= middle:
        temp[temp_index] = arr[left]
        left += 1
        temp_index += 1

    while right <= end:
        temp[temp_index] = arr[right]
        right += 1
        temp_index += 1

    for i in range(len(temp)):
        arr[start + i] = temp[i]

def mergeSort(arr, start, end):
    if start >= end:
        return

    middle = (start + end) // 2
    mergeSort(arr, start, middle)
    mergeSort(arr, middle + 1, end)
    merge(arr, start, middle, end)

input_sizes = list(range(5000, 200001, 15000))
execution_times = []

for size in input_sizes:
    arr = [random.randint(0, size) for _ in range(size)]
    start_time = time.time()
    mergeSort(arr, 0, len(arr) - 1)
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000
    execution_times.append(elapsed_time)
    print(f"Size: {size}, Time: {elapsed_time:.4f} ms")

nlogn_values = [n * math.log2(n) for n in input_sizes]

max_time = max(execution_times)
max_growth = max(nlogn_values)

normalized_times = [time / max_time for time in execution_times]
normalized_growth = [growth / max_growth for growth in nlogn_values]

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, normalized_times, label='Merge Sort Timing (normalized)', color='blue')
plt.plot(input_sizes, normalized_growth, label='O(n log n) Growth (normalized)', color='green', linestyle='--')
plt.title("Merge Sort Growth Comparison with O(n log n)")
plt.xlabel("Input Size (n)")
plt.ylabel("Normalized Values")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
