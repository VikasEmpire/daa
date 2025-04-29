import random
import time
import matplotlib.pyplot as plt

def bucket_sort(arr):
    if not arr: return []
    num_buckets = 10
    min_val, max_val = min(arr), max(arr)
    range_size = (max_val - min_val + 1) / num_buckets

    buckets = [[] for _ in range(num_buckets)]
    for num in arr:
        index = min(int((num - min_val) / range_size), num_buckets - 1)
        buckets[index].append(num)

    return [num for bucket in buckets for num in sorted(bucket)]

def generate_input(size, case):
    if case == 'best':
        return [random.uniform(0, size) for _ in range(size)]
    elif case == 'average':
        return [random.randint(0, size) for _ in range(size)]
    elif case == 'worst':
        return [size // 2] * size

def measure_time(arr):
    start = time.time()
    bucket_sort(arr)
    return (time.time() - start) * 1000  # in milliseconds

sizes = list(range(5000, 50001, 5000))
cases = ['best', 'average', 'worst']
results = {case: [] for case in cases}

for size in sizes:
    print(f"Size: {size}", end=', ')
    for case in cases:
        time_taken = measure_time(generate_input(size, case))
        results[case].append(time_taken)
        print(f"{case.capitalize()}: {time_taken:.2f} ms", end=', ')
    print()

# Normalize data for plotting
max_time = max(max(times) for times in results.values())
max_n = max(sizes)
max_n2 = max_n ** 2

plt.figure(figsize=(12, 6))
colors = {'best': 'g', 'average': 'b', 'worst': 'r'}
styles = {'best': '-', 'average': '--', 'worst': ':'}

for case in cases:
    normalized = [t / max_time for t in results[case]]
    plt.plot(sizes, normalized, color=colors[case], linestyle=styles[case], label=f"{case.capitalize()} Case")

plt.plot(sizes, [n / max_n for n in sizes], 'k-.', label="O(n)")
plt.plot(sizes, [(n**2)/max_n2 for n in sizes], 'm-.', label="O(n²)")

plt.title("Bucket Sort Performance (Normalized)")
plt.xlabel("Input Size")
plt.ylabel("Normalized Time")
plt.legend()
plt.grid(True)
plt.show()
