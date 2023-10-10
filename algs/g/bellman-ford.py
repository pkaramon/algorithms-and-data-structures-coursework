def bellman_ford(graph, s):
    n = len(graph)
    dist = [float('inf')] * n
    parent = [None] * n
    dist[s] = 0

    for _ in range(n - 1):
        for v in range(n):
            for u in range(n):
                if dist[v] + graph[v][u] < dist[u]:
                    dist[u] = dist[v] + graph[v][u]
                    parent[u] = v

    return dist, parent, detect_negative_cycle(graph, dist)


def detect_negative_cycle(graph, dist):
    n = len(graph)
    for _ in range(n - 1):
        for v in range(n):
            for u in range(n):
                if dist[v] + graph[v][u] < dist[u]:
                    return True
    return False
