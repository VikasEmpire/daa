import random
import time
import matplotlib.pyplot as plt

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Input sizes
input_sizes = list(range(5000, 200001, 15000))

# Best case: All numbers have the same digit length (e.g., small range)
def generate_best_case(size):
    return [random.randint(1, 999) for _ in range(size)]  # 3-digit numbers

# Worst case: Numbers with widely varying digit lengths
def generate_worst_case(size):
    return [random.choice([1, 10**6]) for _ in range(size)]  # Either 1 or 1,000,000

# Average case: Random numbers (original case)
def generate_average_case(size):
    return [random.randint(0, size) for _ in range(size)]

# Measure execution time for all cases
best_case_times = []
worst_case_times = []
average_case_times = []

for size in input_sizes:
    # Best case
    arr = generate_best_case(size)
    start = time.time()
    radix_sort(arr)
    end = time.time()
    best_case_times.append((end - start) * 1000)

    # Worst case
    arr = generate_worst_case(size)
    start = time.time()
    radix_sort(arr)
    end = time.time()
    worst_case_times.append((end - start) * 1000)

    # Average case
    arr = generate_average_case(size)
    start = time.time()
    radix_sort(arr)
    end = time.time()
    average_case_times.append((end - start) * 1000)

    print(f"Size: {size}, Best: {best_case_times[-1]:.2f} ms, Worst: {worst_case_times[-1]:.2f} ms, Avg: {average_case_times[-1]:.2f} ms")

# Plot all cases
plt.figure(figsize=(12, 6))
plt.plot(input_sizes, best_case_times, label="Best Case (Small Digits)", color="green")
plt.plot(input_sizes, average_case_times, label="Average Case (Random)", color="blue")
plt.plot(input_sizes, worst_case_times, label="Worst Case (Large Digits)", color="red")

plt.title("Radix Sort: Best, Average & Worst Case Performance")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (ms)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()