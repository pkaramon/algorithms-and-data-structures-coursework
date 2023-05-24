from queue import PriorityQueue


def dijkstra(graph, s, t):
    n = len(graph)
    d = [float('inf')] * n
    d[s] = 0
    parent = [None] * n
    q = PriorityQueue()
    q.put((0, s))

    while not q.empty():
        du, u = q.get()
        if du != d[u]:
            continue

        for v, w in graph[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                parent[v] = u
                q.put((d[v], v))
    return d[t], parent


graph = [
    [(1, 2), (2, 4)],
    [(0, 2), (3, 4), (2, 1)],
    [(0, 4), (1, 1), (3, 2), (4, 1), ],
    [(1, 4), (2, 2), (5, 1)],
    [(2, 1), (5, 3)],
    [(3, 1), (4, 3)]
]

print(dijkstra(graph, 0, 5))


def diks(graph, s):
    n = len(graph)
    d = [float('inf')] * n
    parent = [None] * n

    q = PriorityQueue()
    q.put((0, s))

    while not q.empty():
        dv, v = q.get()
        if dv != d[v]:
            continue

        for u, w in graph[v]:
            if d[u] > d[v] + w:
                d[u] = d[v] + w
                parent[u] = v
                q.put((d[u], u))
