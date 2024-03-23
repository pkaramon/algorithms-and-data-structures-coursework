""" Piotr Karamon

Algorytm zamienia listę krawędzi na graf w postaci listy list sąsiedzctwa.
Następnie uruchamia algorytm Dijkstry uwzględniając osobliwości tylko raz.

Czas:   O(ElogV)
Pamięć: O(E+V)
"""
import heapq

from zad5testy import runtests


def spacetravel(n, E, S, a, b):
    graph, quick_travel = transform_graph(n, E, S)
    d = dijkstra(graph, quick_travel, S, a, b)
    return d if d != float('inf') else None


def transform_graph(n, E, S):
    graph = [[] for _ in range(n)]
    for u, v, t in E:
        graph[u].append((v, t))
        graph[v].append((u, t))

    quick_travel = [False] * n
    for planet in S:
        quick_travel[planet] = True
    return graph, quick_travel


def dijkstra(graph, quick_travel, S, a, b):
    n = len(graph)
    d = [float('inf')] * n
    d[a] = 0
    q = []

    heapq.heappush(q, (0, a))
    quick_travel_used = False
    while len(q) != 0:
        p, u = heapq.heappop(q)
        if d[u] != p:
            continue
        if not quick_travel_used and quick_travel[u]:
            quick_travel_used = True
            for v in S:
                if v != u and d[v] > d[u]:
                    d[v] = d[u]
                    heapq.heappush(q, (d[v], v))

        for v, w in graph[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                heapq.heappush(q, (d[v], v))

    return d[b]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
