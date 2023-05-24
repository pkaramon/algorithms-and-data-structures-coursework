"""
Bellman-Ford

Shortest path in a directed graph with no negative cycles.

We are relaxing each edge n-1 times.
Relaxation is the same as in Dijkstra.

Suppose this is the shortest path from u -> v

u -> a1 -> a2 | -> a3 -> a4 -> v

"""


# graph is a matrix???
def detect_negative_cycle(graph, dist):
    n = len(graph)
    for _ in range(n - 1):
        for v in range(n):
            for u in range(n):
                if dist[v] + graph[v][u] < dist[u]:
                    return True
    return False


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

    detect_negative_cycle(graph, dist)
    return dist, parent


graph = [
    (0, 1, 6),
    (0, 2, 7),
    ()
]
