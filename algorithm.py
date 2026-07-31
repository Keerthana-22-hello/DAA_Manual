import heapq
import random 

# =====================================================
# Disjoint Set (Union-Find)
# =====================================================

class DisjointSet:

    def __init__(self, n):

        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):

        if self.parent[x] != x:

            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:

            self.parent[root_x] = root_y

        elif self.rank[root_x] > self.rank[root_y]:

            self.parent[root_y] = root_x

        else:

            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


# =====================================================
# Build Adjacency List
# =====================================================

def build_adj(edges):

    adj = {}

    for weight, u, v in edges:

        if u not in adj:
            adj[u] = []

        if v not in adj:
            adj[v] = []

        adj[u].append((v, weight))
        adj[v].append((u, weight))

    return adj


# =====================================================
# Kruskal Algorithm
# =====================================================

def kruskal(vertices, edges):

    edges.sort()

    ds = DisjointSet(vertices)

    mst = []

    total_cost = 0

    for weight, u, v in edges:

        if ds.union(u, v):

            mst.append((u, v, weight))

            total_cost += weight

            if len(mst) == vertices - 1:
                break

    return mst, total_cost


# =====================================================
# Prim Algorithm
# =====================================================

def prim(vertices, adj):

    if vertices == 0:
        return [], 0

    visited = set()

    mst = []

    total_cost = 0

    start = 0

    visited.add(start)

    heap = []

    for neighbor, weight in adj.get(start, []):

        heapq.heappush(
            heap,
            (weight, start, neighbor)
        )

    while heap and len(visited) < vertices:

        weight, u, v = heapq.heappop(heap)

        if v in visited:
            continue

        visited.add(v)

        mst.append((u, v, weight))

        total_cost += weight

        for nxt, wt in adj.get(v, []):

            if nxt not in visited:

                heapq.heappush(
                    heap,
                    (wt, v, nxt)
                )

    return mst, total_cost


# =====================================================
# Dijkstra Algorithm
# =====================================================

def dijkstra(graph, source):

    distance = {

        node: float("inf")

        for node in graph

    }

    previous = {

        node: None

        for node in graph

    }

    distance[source] = 0

    priority_queue = [

        (0, source)

    ]

    while priority_queue:

        current_distance, current = heapq.heappop(
            priority_queue
        )

        if current_distance > distance[current]:
            continue

        for neighbor, weight in graph[current]:

            new_distance = current_distance + weight

            if new_distance < distance[neighbor]:

                distance[neighbor] = new_distance

                previous[neighbor] = current

                heapq.heappush(
                    priority_queue,
                    (
                        new_distance,
                        neighbor
                    )
                )

    distance_list = []

    previous_list = []

    for i in sorted(graph.keys()):

        distance_list.append(distance[i])

        previous_list.append(previous[i])

    return distance_list, previous_list


# =====================================================
# Reconstruct Shortest Path
# =====================================================

def reconstruct_path(previous, source, destination):

    path = []

    current = destination

    while current is not None:

        path.append(current)

        current = previous[current]

    path.reverse()

    if path and path[0] == source:

        return path

    return []

# =====================================================
# Min-Max Value by Applying Divide and Conquer Technique 
# =====================================================
comparison_count = 0


def min_max_dc(arr, low, high):
    """
    Find the minimum and maximum element in an array
    using the Divide and Conquer technique.
    """
    global comparison_count

    # Base case: Only one element
    if low == high:
        return arr[low], arr[low]

    # Base case: Two elements
    if high == low + 1:
        comparison_count += 1

        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide the array into two halves
    mid = (low + high) // 2

    left_min, left_max = min_max_dc(arr, low, mid)
    right_min, right_max = min_max_dc(arr, mid + 1, high)

    # Combine the results
    comparison_count += 1
    overall_min = left_min if left_min < right_min else right_min

    comparison_count += 1
    overall_max = left_max if left_max > right_max else right_max

    return overall_min, overall_max


def min_max_naive(arr):
    """
    Find minimum and maximum using the normal linear method.
    """
    minimum = maximum = arr[0]
    comparisons = 0

    for x in arr[1:]:
        comparisons += 1
        if x < minimum:
            minimum = x

        comparisons += 1
        if x > maximum:
            maximum = x

    return minimum, maximum, comparisons




# =====================================================
# Testing
# =====================================================

if __name__ == "__main__":

    edges = [

        (7, 0, 1),
        (5, 0, 3),
        (8, 1, 2),
        (9, 1, 3),
        (7, 1, 4),
        (5, 2, 4),
        (15, 3, 4),
        (6, 3, 5),
        (8, 4, 5),
        (9, 4, 6),
        (11, 5, 6)

    ]

    adjacency = build_adj(edges)

    mst, cost = kruskal(7, edges.copy())

    print("Kruskal MST")
    print(mst)
    print("Cost =", cost)

    mst, cost = prim(7, adjacency)

    print("\nPrim MST")
    print(mst)
    print("Cost =", cost)

    graph = {

        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [(4, 3)],
        4: [(5, 2)],
        5: []

    }

    dist, prev = dijkstra(graph, 0)

    print("\nDistances")
    print(dist)

    print("\nPath 0 → 5")
    print(reconstruct_path(prev, 0, 5))