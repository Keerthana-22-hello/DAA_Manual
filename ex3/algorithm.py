import heapq


# -----------------------------
# Union Find (Disjoint Set)
# -----------------------------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        return True


# -----------------------------
# Kruskal Algorithm
# -----------------------------
def kruskal(n, edges):

    edges = sorted(edges)

    uf = UnionFind(n)

    mst = []
    cost = 0

    for weight, u, v in edges:

        if uf.union(u, v):

            mst.append((u, v, weight))
            cost += weight

            if len(mst) == n - 1:
                break

    return mst, cost


# -----------------------------
# Prim Algorithm
# -----------------------------
def prim(n, adj, start=0):

    visited = [False] * n

    parent = [-1] * n

    key = [float("inf")] * n

    key[start] = 0

    pq = [(0, start)]

    mst = []

    cost = 0

    while pq:

        weight, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        if parent[u] != -1:
            mst.append((parent[u], u, weight))
            cost += weight

        for v, wt in adj.get(u, []):

            if not visited[v] and wt < key[v]:

                key[v] = wt
                parent[v] = u

                heapq.heappush(pq, (wt, v))

    return mst, cost


# -----------------------------
# Build Adjacency List
# -----------------------------
def build_adj(edges):

    adj = {}

    for w, u, v in edges:

        adj.setdefault(u, []).append((v, w))
        adj.setdefault(v, []).append((u, w))

    return adj