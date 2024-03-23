from algs.g.findunion import find_set, union, Node


def kruskal(graph):
    """
    @param graph: adjacency list
    @return: set of mst edges
    """

    n = len(graph)
    edges = []
    for v in range(n):
        for u, w in graph[v]:
            if v < u:
                edges.append((v, u, w))

    edges.sort(key=lambda e: e[2])

    mst_edges = []
    nodes = [Node() for _ in range(n)]

    for v, u, w in edges:
        if find_set(nodes[v]) is not find_set(nodes[u]):
            mst_edges.append((v, u, w))
            union(nodes[v], nodes[u])
    return mst_edges


#
# g = [
#     [(1, 1), (5, 8), (4, 5)],
#     [(0, 1), (2, 3)],
#     [(1, 3), (4, 4), (3, 6)],
#     [(4, 2), (2, 6)],
#     [(0, 5), (2, 4), (5, 7), (3, 2)],
#     [(0, 8), (4, 7)]
# ]


g = [
    [0, 6, 10, 0, 0, 0, 0, 0, 0, 0, ],
    [6, 0, 12, 11, 14, 0, 0, 0, 0, 0, ],
    [10, 12, 0, 12, 0, 0, 8, 16, 0, 0, ],
    [0, 11, 12, 0, 0, 6, 3, 0, 0, 0, ],
    [0, 14, 0, 0, 0, 4, 0, 0, 6, 0, ],
    [0, 0, 0, 6, 4, 0, 0, 0, 12, 0, ],
    [0, 0, 8, 3, 0, 0, 0, 0, 16, 6, ],
    [0, 0, 16, 0, 0, 0, 0, 0, 0, 8, ],
    [0, 0, 0, 0, 6, 12, 16, 0, 0, 13, ],
    [0, 0, 0, 0, 0, 0, 6, 8, 13, 0, ],
]


def from_matrix_to_adj(matrix):
    n = len(matrix)
    g = [[] for _ in range(n)]
    for v in range(n):
        for u in range(n):
            if matrix[v][u] != 0:
                g[v].append((u, matrix[v][u]))
    return g


g = from_matrix_to_adj(g)
print(kruskal(g))
