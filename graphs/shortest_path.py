from collections import deque


def find_shortest_path(graph, a, b):
    order = len(graph)
    visited = [False] * order
    parent = [None] * order

    queue = deque()
    queue.append(a)
    visited[a] = True

    while len(queue) != 0:
        v = queue.popleft()
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                parent[u] = v
                queue.append(u)
            if u == b:
                return construct_path_from_parent(parent, a, b)
    return None


def construct_path_from_parent(parent, a, b):
    path = []
    i = b
    while i != parent[a]:
        path.append(i)
        i = parent[i]
    path.reverse()
    return path


graph = [
    [1, 2],
    [0, 5, 6],
    [0, 5, 3],
    [2, 5, 4],
    [3, 8, 9],
    [1, 2, 3, 7],
    [1, 8],
    [5, 8],
    [6, 7, 4, 9],
    [4, 8]
]
print("OH NO")
print(find_shortest_path(graph, 0, 5))
