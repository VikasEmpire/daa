import heapq
import random
import time
import matplotlib.pyplot as plt

def test_priority_queue(size, max_value):
    # Create random data
    data = [random.randint(1, max_value) for _ in range(size)]
    
    # Time heap push operations
    start = time.time()
    heap = []
    for num in data:
        heapq.heappush(heap, num)
    push_time = (time.time() - start) * 1000
    
    # Time heap pop operations
    start = time.time()
    while heap:
        heapq.heappop(heap)
    pop_time = (time.time() - start) * 1000
    
    return push_time, pop_time

# Test parameters
sizes = [1000, 5000, 10000, 15000, 20000]
results = {
    'Push (small range)': [],
    'Pop (small range)': [],
    'Push (large range)': [],
    'Pop (large range)': []
}

# Run tests
for size in sizes:
    # Small range (k=100)
    push, pop = test_priority_queue(size, 100)
    results['Push (small range)'].append(push)
    results['Pop (small range)'].append(pop)
    
    # Large range (k=1M)
    push, pop = test_priority_queue(size, 1000000)
    results['Push (large range)'].append(push)
    results['Pop (large range)'].append(pop)
    
    print(f"Size: {size}, Push Small: {results['Push (small range)'][-1]:.1f}ms, Pop Large: {results['Pop (large range)'][-1]:.1f}ms")

# Calculate theoretical curves
scale_log = results['Push (small range)'][-1] / (sizes[-1] * (sizes[-1]**0.1))  # Approx O(n log n)
scale_n = results['Push (small range)'][-1] / sizes[-1]
scale_n2 = results['Push (large range)'][-1] / (sizes[-1]**2)

theory_n = [size * scale_n for size in sizes]
theory_nlogn = [size * (size**0.1) * scale_log for size in sizes]  # Approximate log n
theory_n2 = [(size**2) * scale_n2 for size in sizes]

# Plot results
plt.figure(figsize=(10,6))
plt.plot(sizes, results['Push (small range)'], '-', label='Push (k=100)')
plt.plot(sizes, results['Pop (small range)'], '--', label='Pop (k=100)')
plt.plot(sizes, results['Push (large range)'], ':', label='Push (k=1M)')
plt.plot(sizes, results['Pop (large range)'], '-.', label='Pop (k=1M)')
plt.plot(sizes, theory_n, '--', label='Theoretical O(n)', alpha=0.5)
plt.plot(sizes, theory_nlogn, '--', label='Theoretical O(n log n)', alpha=0.5)
plt.plot(sizes, theory_n2, '--', label='Theoretical O(n²)', alpha=0.5)

plt.title('Priority Queue (Min-Heap) Performance')
plt.xlabel('Input Size')
plt.ylabel('Time (ms)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()