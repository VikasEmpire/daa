import random
import time
import matplotlib.pyplot as plt

def counting_sort(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10
    
    for num in arr:
        count[(num // exp) % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i-1]
    
    for num in reversed(arr):
        output[count[(num // exp) % 10]-1] = num
        count[(num // exp) % 10] -= 1
    
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Test parameters
sizes = list(range(5000, 200001, 15000))
results = {'Best': [], 'Average': [], 'Worst': []}

# Test cases
def best_case(size): return [random.randint(100, 999) for _ in range(size)]
def avg_case(size): return [random.randint(0, size) for _ in range(size)]
def worst_case(size): return [random.choice([1, 10**6]) for _ in range(size)]

# Run tests
for size in sizes:
    # Best case (3-digit numbers)
    arr = best_case(size)
    start = time.time()
    radix_sort(arr)
    results['Best'].append((time.time()-start)*1000)
    
    # Average case
    arr = avg_case(size)
    start = time.time()
    radix_sort(arr)
    results['Average'].append((time.time()-start)*1000)
    
    # Worst case (mixed digit lengths)
    arr = worst_case(size)
    start = time.time()
    radix_sort(arr)
    results['Worst'].append((time.time()-start)*1000)
    
    print(f"Size: {size:6d} | Best: {results['Best'][-1]:6.2f} ms | Avg: {results['Average'][-1]:6.2f} ms | Worst: {results['Worst'][-1]:6.2f} ms")

# Plot results
plt.figure(figsize=(10,5))
plt.plot(sizes, results['Best'], '-', label='Best Case (3-digit)')
plt.plot(sizes, results['Average'], '--', label='Average Case')
plt.plot(sizes, results['Worst'], ':', label='Worst Case (mixed digits)')

plt.title('Radix Sort Performance')
plt.xlabel('Input Size')
plt.ylabel('Time (ms)')
plt.legend()
plt.grid(True)
plt.show()