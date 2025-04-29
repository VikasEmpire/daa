class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u

def kruskal(vertices, edges):
    ds = DisjointSet(vertices)
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    mst = []
    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            mst.append((u, v, w))
            ds.union(u, v)
    return mst

if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 5),
        ('B', 'C', 2),
        ('B', 'D', 4),
        ('C', 'D', 3),
        ('D', 'E', 6)
    ]

    mst = kruskal(vertices, edges)
    print("Minimum Spanning Tree:", mst)
