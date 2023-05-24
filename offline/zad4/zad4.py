"""Piotr Karamon

Wyszukuję najkrótszą ścieżkę BFSem.
Jeżeli nie znalaziono żadnej zwaracam None.
Jeżeli znaleziono:
    przeszkodzę przez każdą krawędź tej ścieżki, usuwam ją,
    uruchamiam BFS w celu znaleziona najkrótszej ścieżki.
    Jeżeli się wydłużyła to zwracam tę usuniętą krawędź.
    Jeżeli nie, to przywracam tę krawędź i przechodzę do następnej.

Czas  : O((V+E)*V)
Pamięć: O(V)
"""

from zad4testy import runtests
from collections import deque


def longer(G, s, t):
    shortest = find_shortest_path(G, t, s)
    if shortest is None:
        return None

    for i in range(len(shortest) - 1):
        v, u = shortest[i], shortest[i + 1]
        G[v].remove(u)
        G[u].remove(v)

        new_shortest = find_shortest_path(G, t, s)
        if new_shortest is None or len(new_shortest) > len(shortest):
            return v, u
        G[v].append(u)
        G[u].append(v)

    return None


def find_shortest_path(G, s, t):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    q = deque()
    q.append(s)
    visited[s] = True

    while len(q) != 0:
        v = q.popleft()
        if v == t:
            break

        for u in G[v]:
            if not visited[u]:
                q.append(u)
                parent[u] = v
                visited[u] = True
    else:
        return None

    path = []
    i = t
    while i != parent[s]:
        path.append(i)
        i = parent[i]

    return path[::-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
