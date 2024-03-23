from collections import deque


def bfs_shortest_path(graph: list[list[(int, int)]], s: int, t: int):
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


graph = [
    [(1, 2), (2, 4)],
    [(0, 2), (3, 4), (2, 1)],
    [(0, 4), (1, 1), (3, 2), (4, 1), ],
    [(1, 4), (2, 2), (5, 1)],
    [(2, 1), (5, 3)],
    [(3, 1), (4, 3)]
]

print(bfs_shortest_path(graph, 0, 5))
