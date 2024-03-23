from queue import PriorityQueue


def find_mst(graph):
    n = len(graph)
    processed = [False] * n
    parent = [None] * n
    d = [float('inf')] * n

    pq = PriorityQueue()
    pq.put((0, 0))

    while not pq.empty():
        dv, v = pq.get()
        for u in range(n):
            if 0 < graph[u][v] < d[u] and not processed[u]:
                d[u] = graph[u][v]
                parent[u] = v
                pq.put((d[u], u))
        processed[v] = True
    return from_parent_to_mst(graph, parent)


def from_parent_to_mst(graph, parent):
    n = len(graph)
    mst = [[] for _ in range(n)]
    for v in range(1, n):
        pv = parent[v]
        mst[v].append((pv, graph[v][pv]))
        mst[pv].append((v, graph[v][pv]))
    return mst
