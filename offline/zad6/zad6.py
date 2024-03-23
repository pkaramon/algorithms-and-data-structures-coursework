""" Piotr Karamon
Algorytm tworzy graf o rozmiarze 2n dla łatwości implementacji.
Następnie za pomocą BFS szukane są ścieżki powiększające.
Jeżeli takowa zostanie znaleziona to powiększa skojarzenie.
Algorytm się kończy w momencie gdy nie zostaje znaleziona ścieżka powiększająca.

Czas: O(n^3)
Pamięć: (n^2)
"""

from collections import deque

from zad6testy import runtests


def binworker(M):
    graph = create_graph(M)
    matching = greedy(M)
    ok, parent, v = find_aug_bfs(graph, matching)
    while ok:
        opt_match(parent, v, matching)
        ok, parent, v = find_aug_bfs(graph, matching)
    return sum(1 for x in matching if x is not None) // 2


def create_graph(workers):
    n = len(workers)
    graph = [[workers[w][i] + n for i in range(len(workers[w]))] for w in range(n)]
    machines = get_machines(workers)
    graph.extend(machines)
    return graph


def greedy(workers):
    n = len(workers)
    matching = [None] * (2 * n)
    for w in range(n):
        for m in workers[w]:
            if matching[m + n] is None:
                matching[m + n] = w
                matching[w] = m + n
                break
    return matching


def find_aug_bfs(graph, matching):
    size = len(graph)
    n = size // 2
    visited = [False] * size
    parent = [None] * size

    q = deque()
    for w in range(n):
        if matching[w] is None:
            q.append(w)
            visited[w] = True

    while len(q) > 0:
        v = q.popleft()
        if n <= v and matching[v] is None:
            return True, parent, v

        for neigh in graph[v]:
            if visited[neigh]:
                continue
            if (n <= v and matching[neigh] == v) or (v < n and v != matching[neigh]):
                visited[neigh] = True
                parent[neigh] = v
                q.append(neigh)
    return False, None, None


def opt_match(parent, v, matching):
    path = []
    x = v
    while x is not None:
        path.append(x)
        x = parent[x]
    path.reverse()

    for i in range(len(path) - 1):
        if i % 2 == 0:
            matching[path[i]] = path[i + 1]
            matching[path[i + 1]] = path[i]
        else:
            matching[path[i + 1]] = None


def get_machines(workers):
    n = len(workers)
    machines = [[] for _ in range(n)]
    for w in range(n):
        for u in workers[w]:
            machines[u].append(w)
    return machines


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=True)
