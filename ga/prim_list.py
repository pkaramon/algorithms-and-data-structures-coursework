import heapq


def find_mst_prim(graph):
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
