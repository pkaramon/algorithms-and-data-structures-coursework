from collections import deque

from zad4testy import runtests


def longer(G, s, t):
    shortest = find_shortest_path(G, s, t)
    if shortest is None:
        return None
    print(shortest)

    for i in range(len(shortest) - 1):
        v, u = shortest[i], shortest[i + 1]
        G[v].remove(u)
        G[u].remove(v)

        if find_shortest_path_without_edge(G, s, t) > len(shortest) - 1:
            return v, u
        G[v].append(u)
        G[u].append(v)

    return None


def find_shortest_path(G, s, t, ):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    q = deque()
    q.appendleft(s)
    visited[s] = True

    while len(q) != 0:
        v = q.pop()
        if v == t:
            break

        for u in G[v]:
            if not visited[u]:
                q.appendleft(u)
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


def find_shortest_path(G, s, t, ):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    dist = [0] * n
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
                dist[u] = dist[v] + 1
    else:
        return None

    path = []
    i = t
    while i != parent[s]:
        path.append(i)
        i = parent[i]

    return path[::-1]


def find_shortest_path_without_edge(G, s, t, ):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    dist = [0] * n

    q = deque()
    q.appendleft(s)
    visited[s] = True

    while len(q) != 0:
        v = q.pop()
        if v == t:
            break
        for u in G[v]:
            if not visited[u]:
                q.appendleft(u)
                parent[u] = v
                visited[u] = True
                dist[u] = dist[v] + 1
    else:
        return float('inf')

    return dist[t]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
