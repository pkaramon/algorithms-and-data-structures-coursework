"""
PRECONDITIONS
A graph undirected or directed must be connected in order to have an euler cycle/path.

In undirected graph there exists an euler cycle iff
    For every v in Vertices deg(v) is even

In undirected graph there exists an euler path iff
   There exist exactly two vertices u and v
   whose degrees are odd

In directed graph there exists an euler cycle iff
    For every v in Vertices in_deg(v) = out_deg(v)

In undirected graph there exists an euler path iff
   There exist exactly two vertices u and v
   such that out_deg(v)-in_deg(v) = 1
             in_deg(u)-out_deg(v) = 1

ALGORITHM
1. Run DFS from a selected vertex. When moving to another vertex we "remove" the edge that
we use. When we get stuck(vertex with no edges) we add it to the front of cycle.
"""


def euler_matrix_undirected(matrix):
    order = len(matrix)
    edge_indexes = [0] * order
    cycle = []

    def dfs_visit(v):
        for u in range(edge_indexes[v], order):
            edge_indexes[v] += 1
            if matrix[v][u]:
                matrix[v][u] = 0
                matrix[u][v] = 0  # omit if graph is directed
                dfs_visit(u)
        cycle.append(v)

    dfs_visit(0)
    return cycle[::-1]


def euler_adj_directed(graph):
    order = len(graph)
    edge_indexes = [0] * order
    cycle = []
    done = [False] * order

    def dfs_visit(v):
        for i in range(edge_indexes[v], len(graph[v])):
            u = graph[v][i]
            edge_indexes[v] += 1
            if not done[u]:
                dfs_visit(u)
        done[v] = True
        cycle.append(v)

    dfs_visit(0)
    return cycle[::-1]


class RemovedIndicator:
    def __init__(self):
        self.removed = False

    def __repr__(self):
        return f'{self.removed}'


def transform_undirected_adj_list(graph):
    n = len(graph)
    transformed =  [[] for _ in range(n)]

    for v in range(n):
        for u in graph[v]:
            if v < u:
                ind = RemovedIndicator()
                transformed[v].append((u, ind))
                transformed[u].append((v, ind))
    return transformed


def euler_adj_undirected(graph):
    order = len(graph)
    graph = transform_undirected_adj_list(graph)
    edge_indexes = [0] * order
    cycle = []
    done = [False] * order

    def dfs_visit(v):
        for i in range(edge_indexes[v], len(graph[v])):
            u, indicator = graph[v][i]
            edge_indexes[v] += 1
            if not done[u] and not indicator.removed:
                indicator.removed = True
                dfs_visit(u)

        done[v] = True
        cycle.append(v)

    dfs_visit(0)
    return cycle[::-1]


def list_of_edges_to_matrix(n, edges):
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1
    return matrix


print(euler_matrix_undirected(list_of_edges_to_matrix(
    7,
    [
        (0, 1),
        (0, 2),
        (1, 3),
        (1, 5),
        (1, 4),
        (2, 3),
        (2, 5),
        (2, 6),
        (4, 6),
        (5, 6),
        (5, 4),
        (2, 4),
        (6, 1),
        (1, 2)
    ]
)))

print(euler_adj_undirected([
    [1, 3],
    [0, 2],
    [1, 3],
    [0, 2]
]))

g = [
    [1, 3],
    [0, 2],
    [1, 3],
    [0, 2]
]

g = transform_undirected_adj_list(g)