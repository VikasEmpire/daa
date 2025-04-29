import heapq

def prim_mst(graph):
    V = len(graph)
    visited = [False] * V
    min_heap = [(0, 0)]  # (weight, vertex)
    mst_cost = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_cost += weight

        for v, w in enumerate(graph[u]):
            if not visited[v] and w > 0:
                heapq.heappush(min_heap, (w, v))
                mst_edges.append((u, v, w))

    return mst_cost, mst_edges

if __name__ == "__main__":
    graph =[
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    cost, edges = prim_mst(graph)
    print("Prim's Minimum Spanning Tree Cost:", cost)
    print("Edges in MST:")
    for u, v, w in edges:
        print(f"{u} - {v}: {w}")
