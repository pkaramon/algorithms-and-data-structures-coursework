"""
Graph is an undirected graph in matrix repr.
I am assuming that there exists an euler cycle, i.e.
graph is connected and degree of every vertex is even.

processed -> every single edge in that vertex was deleted
"""


def find_euler_cycle_adj(graph):
    n = len(graph)
    graph = modify_graph(graph)
    edge_indexes = [0] * n
    cycle = []
    print(graph)

    def dfs_visit(v):
        for i in range(edge_indexes[v], len(graph[v])):
            edge_indexes[v] += 1
            u, ind = graph[v][i]
            if not ind.removed:
                ind.removed = True
                dfs_visit(u)
        cycle.append(v)

    dfs_visit(0)
    cycle.reverse()
    return cycle


class RemovedIndicator:
    def __init__(self):
        self.removed = False

    def __repr__(self):
        return f'{self.removed}'


def modify_graph(graph):
    n = len(graph)
    g = [[] for _ in range(n)]
    for v in range(n):
        for u in graph[v]:
            if v < u:
                ind = RemovedIndicator()
                g[v].append((u, ind))
                g[u].append((v, ind))
    return g


def find_euler_cycle_undirected(graph):
    n = len(graph)
    edge_indexes = [0] * n
    cycle = []

    def dfs_visit(v):
        for u in range(edge_indexes[v], n):
            edge_indexes[v] += 1
            if graph[v][u]:
                graph[v][u] = 0
                graph[u][v] = 0
                dfs_visit(u)
        cycle.append(v)

    dfs_visit(0)
    cycle.reverse()
    return cycle


graph = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0, ],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, ],
    [0, 1, 0, 1, 1, 0, 0, 1, 0, ],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, ],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, ],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, ],
    [0, 0, 0, 0, 1, 1, 0, 1, 1, ],
    [0, 1, 1, 0, 1, 0, 1, 0, 0, ],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, ],
]


def from_matrix_to_adj(matrix):
    n = len(matrix)
    g = [[] for _ in range(n)]
    for v in range(n):
        for u in range(n):
            if matrix[v][u]:
                g[v].append(u)
    return g


# print(find_euler_cycle_undirected(graph))
print(find_euler_cycle_adj(from_matrix_to_adj(graph)))
