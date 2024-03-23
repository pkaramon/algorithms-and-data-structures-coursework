from collections import deque


def bfs_shortest_path(graph, s, t):
    n = len(graph)
    q = deque()
    visited = [False] * n
    parent = [None] * n
    visited[s] = True
    q.append((s, 0))

    while len(q) > 0:
        v, w = q.popleft()

        if w > 0:
            q.append((v, w - 1))
        else:
            visited[v] = True
            for u, w in graph[v]:
                if not visited[u]:
                    q.append((u, w))
                    parent[u] = v
    return parent
