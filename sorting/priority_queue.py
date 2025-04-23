import heapq
import random
import time
import matplotlib.pyplot as plt

# Test parameters
sizes = [1000, 5000, 10000, 15000, 20000]
times = []

for size in sizes:
    data = [random.random() for _ in range(size)]  # Random data
    
    # Time push operations
    start = time.time()
    heap = []
    for x in data:
        heapq.heappush(heap, x)
    push_time = (time.time() - start) * 1000
    
    # Time pop operations
    start = time.time()
    while heap:
        heapq.heappop(heap)
    pop_time = (time.time() - start) * 1000
    
    times.append((push_time + pop_time))
    print(f"Size: {size}, Time: {times[-1]:.1f}ms")

# Theoretical curves (simplified scaling)
n = sizes
nlogn = [size * 0.001 * (size ** 0.1) for size in sizes]  # Approximate O(n log n)
n2 = [size * size * 0.000001 for size in sizes]  # O(n²)

# Plot
plt.figure(figsize=(8,5))
plt.plot(n, times, '-o', label='Priority Queue Operations')
plt.plot(n, nlogn, '--', label='O(n log n)')
plt.plot(n, n2, ':', label='O(n²)')

plt.title('Priority Queue Performance')
plt.xlabel('Input Size')
plt.ylabel('Time (ms)')
plt.legend()
plt.grid(True)
plt.show()