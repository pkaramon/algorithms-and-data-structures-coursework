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
