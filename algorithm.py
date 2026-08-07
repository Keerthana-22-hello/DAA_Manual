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
# Matrix Chain Multiplication (Dynamic Programming)
# =====================================================

def matrix_chain_order(dims):
    """
    Matrix Chain Multiplication using Dynamic Programming

    Parameters
    ----------
    dims : list[int]
        Matrix dimensions where matrix Ai has dimensions
        dims[i-1] x dims[i].

    Returns
    -------
    m : list
        DP cost table.

    s : list
        Split table used to reconstruct
        the optimal parenthesization.
    """

    n = len(dims) - 1

    # Cost table
    m = [
        [0] * (n + 1)
        for _ in range(n + 1)
    ]

    # Split table
    s = [
        [0] * (n + 1)
        for _ in range(n + 1)
    ]

    # Chain length
    for length in range(2, n + 1):

        for i in range(1, n - length + 2):

            j = i + length - 1

            m[i][j] = float("inf")

            for k in range(i, j):

                cost = (

                    m[i][k]

                    + m[k + 1][j]

                    + dims[i - 1] * dims[k] * dims[j]

                )

                if cost < m[i][j]:

                    m[i][j] = cost

                    s[i][j] = k

    return m, s


# =====================================================
# Print Optimal Parenthesization
# =====================================================

def print_optimal_parens(s, i, j):
    """
    Recursively constructs the optimal
    parenthesization.
    """

    if i == j:

        return f"A{i}"

    k = s[i][j]

    left = print_optimal_parens(
        s,
        i,
        k
    )

    right = print_optimal_parens(
        s,
        k + 1,
        j
    )

    return f"({left} × {right})"


# =====================================================
# Convert DP Cost Table to DataFrame
# =====================================================

def cost_table_dataframe(m, n):
    """
    Returns the DP Cost Table
    as a pandas DataFrame.
    """

    import pandas as pd

    rows = []

    for i in range(1, n + 1):

        row = {"Matrix": f"A{i}"}

        for j in range(1, n + 1):

            if j < i:

                row[f"A{j}"] = "---"

            else:

                row[f"A{j}"] = m[i][j]

        rows.append(row)

    return pd.DataFrame(rows)


# =====================================================
# Convert Split Table to DataFrame
# =====================================================

def split_table_dataframe(s, n):
    """
    Returns the Split Table
    as a pandas DataFrame.
    """

    import pandas as pd

    rows = []

    for i in range(1, n + 1):

        row = {"Matrix": f"A{i}"}

        for j in range(1, n + 1):

            if j <= i:

                row[f"A{j}"] = "-"

            else:

                row[f"A{j}"] = s[i][j]

        rows.append(row)

    return pd.DataFrame(rows)


# =====================================================
# Performance Statistics
# =====================================================

def matrix_chain_statistics(dims):
    """
    Returns useful statistics
    about the Matrix Chain problem.
    """

    n = len(dims) - 1

    dp_cells = n * n

    return {

        "matrices": n,

        "dp_cells": dp_cells,

        "time_complexity": "O(n³)",

        "space_complexity": "O(n²)"

    }
    
# =====================================================
# N-Queens Problem using Backtracking
# =====================================================

def is_safe(board, row, col):
    """
    Check whether a queen can be placed at (row, col).

    Parameters
    ----------
    board : list
        Current board representation where board[i] is the
        column position of the queen in row i.
    row : int
        Current row.
    col : int
        Current column.

    Returns
    -------
    bool
        True if the position is safe, otherwise False.
    """

    for prev_row in range(row):

        placed_col = board[prev_row]

        # Same column
        if placed_col == col:
            return False

        # Same diagonal
        if abs(prev_row - row) == abs(placed_col - col):
            return False

    return True


# =====================================================
# Solve N-Queens using Backtracking
# =====================================================

def solve_n_queens(n):
    """
    Solves the N-Queens problem using Backtracking.

    Parameters
    ----------
    n : int
        Number of queens / board size.

    Returns
    -------
    solutions : list
        List of all valid solutions.

    backtracks : int
        Number of backtracking operations performed.
    """

    board = [-1] * n
    solutions = []
    backtrack_count = [0]

    def backtrack(row):

        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):

            if is_safe(board, row, col):

                board[row] = col

                backtrack(row + 1)

                board[row] = -1

                backtrack_count[0] += 1

    backtrack(0)

    return solutions, backtrack_count[0]


# =====================================================
# Convert Solution to Chessboard
# =====================================================

def board_to_matrix(solution, n):
    """
    Converts a solution into a 2D board.

    Returns
    -------
    list
        2D list containing "Q" and ".".
    """

    board = []

    for row in range(n):

        current_row = []

        for col in range(n):

            if solution[row] == col:
                current_row.append("Q")
            else:
                current_row.append(".")

        board.append(current_row)

    return board


# =====================================================
# Get All Chessboards
# =====================================================

def generate_board_matrices(solutions, n):
    """
    Converts every solution into a board matrix.

    Parameters
    ----------
    solutions : list
        List of solution arrays.

    n : int
        Board size.

    Returns
    -------
    list
        List of board matrices.
    """

    boards = []

    for solution in solutions:
        boards.append(board_to_matrix(solution, n))

    return boards


# =====================================================
# Statistics
# =====================================================

def nqueen_statistics(n, solutions, backtracks):
    """
    Returns statistics for the N-Queens problem.

    Parameters
    ----------
    n : int
        Board size.

    solutions : list
        List of solutions.

    backtracks : int
        Number of backtracks.

    Returns
    -------
    dict
        Statistics dictionary.
    """

    return {

        "board_size": n,

        "solutions": len(solutions),

        "backtracks": backtracks,

        "time_complexity": "O(N!)",

        "space_complexity": "O(N)"

    }



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
    
