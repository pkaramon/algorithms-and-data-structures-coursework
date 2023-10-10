""" Piotr Karamon

Każdy wierzchołek w grafie rozbijam na trzy różne w zależności od stanu.

Visiting - to normalne przejście z zamku do zamku
Theft - to przejście z jednego zamku do drugiego oraz obrabowanie go
AfterTheft - to przejście z jednego zamku do drugiego ale po dokonanym rabunku

Wierzchołki Visiting tylko sąsiadują z wierzchołkami Theft i Visiting.
Wierzchołki  Theft sąsiadują z wierzchołkami AfterTheft.
Wierzchołki AfterTheft sąsiadują z wierzchołkami AfterTheft.

Na tym grafie którego rozmiar jest 3*większy od grafu oryginalnego odpalany jest algorytm Dijkstry.
Może w nim występować krawędź ujemna. Jednkaże w ścieżce optymalnej może występować tylko jedna taka krawędź.
Taka krawędź nie zmienia poprawności algorytmu.

Funkcja edge case opisuje przypadek kiedy to zamek startowy zostaje obrabowany.

Czas: O(V^2Logv)
Pamięć: O(V)

"""
from egz1Atesty import runtests

from queue import PriorityQueue
import heapq

VISIT = 0
THEFT = 1
AFTER_THEFT = 2

STATES = [VISIT, THEFT, AFTER_THEFT]


def dijkstra(graph, values, r, s, t):
    n = len(graph)

    d = [
        [float('inf') for _ in range(n)]
        for _ in range(len(STATES))
    ]

    d[VISIT][s] = 0
    q = PriorityQueue()

    q.put((0, VISIT, s))

    while not q.empty():
        du, state, u = q.get()

        if state == VISIT:
            for v, w in graph[u]:
                if d[VISIT][v] > d[VISIT][u] + w:
                    d[VISIT][v] = d[VISIT][u] + w
                    q.put((d[VISIT][v], VISIT, v))

            for v, w in graph[u]:
                if d[THEFT][v] > d[VISIT][u] - values[v] + w:
                    d[THEFT][v] = d[VISIT][u] - values[v] + w
                    q.put((d[THEFT][v], THEFT, v))
        elif state == THEFT:
            for v, w in graph[u]:
                if d[AFTER_THEFT][v] > d[THEFT][u] + 2 * w + r:
                    d[AFTER_THEFT][v] = d[THEFT][u] + 2 * w + r
                    q.put((d[AFTER_THEFT][v], AFTER_THEFT, v))
        elif state == AFTER_THEFT:
            for v, w in graph[u]:
                if d[AFTER_THEFT][v] > d[AFTER_THEFT][u] + 2 * w + r:
                    d[AFTER_THEFT][v] = d[AFTER_THEFT][u] + 2 * w + r
                    q.put((d[AFTER_THEFT][v], AFTER_THEFT, v))

    return min(d[VISIT][t], d[THEFT][t], d[AFTER_THEFT][t])


def edge_case(graph, values, r, s, t):
    n = len(graph)

    d = [ float('inf') for _ in range(n)]

    d[s] = 0

    q = PriorityQueue()
    q.put((0, s))

    while not q.empty():
        du, u = q.get()
        for v, w in graph[u]:
            if d[v] > d[u] + 2 * w + r:
                d[v] = d[u] + 2 * w + r
                q.put((d[v], AFTER_THEFT, v))

        return d[t] - values[s]


def gold(G, V, s, t, r):
    return min(dijkstra(G, V, r, s, t), edge_case(G, V, r, s, t))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)
