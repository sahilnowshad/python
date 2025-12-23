from typing import List, Tuple

class DisjointSet:
    def __init__(self, n):
        # parent[i] = parent of i; if parent[i] == i then i is a root
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y) -> bool:
        # union by rank; return True if union performed (were in different sets)
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

def kruskal(n: int, edges: List[Tuple[int, int, float]]):
    """
    Kruskal's algorithm to compute MST.
    Args:
      n: number of nodes (nodes are 0..n-1)
      edges: list of (u, v, weight)

    Returns:
      mst_edges: list of edges (u, v, weight) in the MST
      total_weight: sum of weights in MST
    """
    # Sort edges by weight
    edges_sorted = sorted(edges, key=lambda e: e[2])
    ds = DisjointSet(n)

    mst_edges = []
    total_weight = 0.0

    for u, v, w in edges_sorted:
        if ds.union(u, v):
            mst_edges.append((u, v, w))
            total_weight += w
            # Optional early stop: if MST has n-1 edges we can break
            if len(mst_edges) == n - 1:
                break

    return mst_edges, total_weight

# Example usage
if __name__ == "__main__":
    # Example undirected weighted graph as an edge list (u, v, weight).
    # Nodes are 0..5 (so n = 6)
    edges = [
        (0, 1, 4),
        (0, 2, 4),
        (1, 2, 2),
        (1, 3, 6),
        (2, 3, 8),
        (2, 4, 3),
        (3, 4, 3),
        (3, 5, 2),
        (4, 5, 7)
    ]
    n = 6

    mst, total = kruskal(n, edges)
    print("Edges in MST:")
    for u, v, w in mst:
        print(f"  {u} - {v} (weight {w})")
    print("Total weight of MST:", total)

    # If graph is disconnected, len(mst) < n-1; handle accordingly
    if len(mst) != n - 1:
        print("Warning: graph is disconnected; no spanning tree exists for all nodes.")
