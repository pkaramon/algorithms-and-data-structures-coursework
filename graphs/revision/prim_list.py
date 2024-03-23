"""
Basically a Dijkstra
but with different relaxation method i.e.:
We are looking at u and x is its neighbour:
if w({u,x}) < d(x) ->
    parent[x] = u
    d[x] = w({u,x})

As with dijkstra when we have a list of lists of neighbours
-> we use priority queue
If we have a matrix we use "linear queue"
-> search through d array and select the smallest distance

When we take a vertex out of the queue we are adding it to the MST.
"""

import heapq


def find_mst_prim(graph):
    """
    @param graph: list of lists of neighbours
    @return: mst
    """
    n = len(graph)
    parent = [None] * n
    d = [float('inf')] * n
    processed = [False] * n
    queue = []
    heapq.heappush(queue, (0, 0))
    d[0] = 0

    while len(queue) > 0:
        dv, v = heapq.heappop(queue)
        for u, w in graph[v]:
            if not processed[u] and w < d[u]:
                d[u] = w
                parent[u] = (v, w)
                heapq.heappush(queue, (w, u))
        processed[v] = True

    return parent


def from_parent_to_mst(parent):
    n = len(parent)
    mst = [[] for _ in range(n)]
    for v in range(1, n):
        v_parent, edge_weight = parent[v]
        mst[v].append((v_parent, edge_weight))
        mst[v_parent].append((v, edge_weight))
    return mst


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

# g = [
#     [(1, 1), (5, 8), (4, 5)],
#     [(0, 1), (2, 3)],
#     [(1, 3), (4, 4), (3, 6)],
#     [(4, 2), (2, 6)],
#     [(0, 5), (2, 4), (5, 7), (3, 2)],
#     [(0, 8), (4, 7)]
# ]

print(from_parent_to_mst(find_mst_prim(g)))
