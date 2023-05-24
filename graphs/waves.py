from collections import deque


def waves(graph):
    order = len(graph)
    current = deque()
    next = deque()

    visited = [False] * order
    visited[0] = True
    current.append(0)

    while len(current) > 0:
        print(current)
        while len(current) > 0:
            v = current.popleft()
            for u in graph[v]:
                if not visited[u]:
                    visited[u] = True
                    next.append(u)
        current, next = next, current
