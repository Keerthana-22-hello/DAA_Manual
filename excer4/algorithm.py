import heapq


def dijkstra(graph, source):
    """
    Dijkstra's Algorithm using Min Heap

    Time Complexity:
        O((V + E) log V)

    Returns:
        dist -> Shortest distances
        prev -> Previous vertex array
    """

    n = len(graph)

    dist = [float("inf")] * n
    prev = [None] * n

    dist[source] = 0

    pq = [(0, source)]
    visited = set()

    while pq:

        current_distance, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        for v, weight in graph[u]:

            if dist[u] + weight < dist[v]:

                dist[v] = dist[u] + weight
                prev[v] = u

                heapq.heappush(
                    pq,
                    (dist[v], v)
                )

    return dist, prev


def reconstruct_path(prev, source, target):

    path = []

    node = target

    while node is not None:
        path.append(node)
        node = prev[node]

    path.reverse()

    if path and path[0] == source:
        return path

    return []