def bellman_ford(graph, s, t):
    n = len(graph)
    d = [float('inf')] * n
    parent = [None] * n

    d[s] = 0

    for i in range(n-1):
        for u in range(n):
            for v, w in graph[u]:
                if d[v] > d[u] + w:
                    d[v] = d[u] + w
                    parent[v] = u

    for u in range(n):
        for v, w in graph[u]:
            if d[v] > d[u] + w:
                return None
    return parent



