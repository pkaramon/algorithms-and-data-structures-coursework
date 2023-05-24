from collections import deque


def has_cycle(graph: list[list[int]]):
    """
    @param graph: list of lists of neighbours
    @return: True if there is a cycle
    """

    order = len(graph)
    visited = [False] * order
    parent = [None] * order

    queue = deque()
    queue.append(0)
    visited[0] = True

    while len(queue) != 0:
        v = queue.popleft()
        for u in graph[v]:
            if visited[u] and u != parent[v]:
                return True
            if not visited[u]:
                visited[u] = True
                parent[u] = v
                queue.append(u)
    return False


graph = [
    [1, 2],
    [0, 3, 4],
    [0, 5, 6, 7],
    [1],
    [1],
    [2, 8],
    [2, 9, 10, 11],
    [2],
    [5],
    [6],
    [6, 12],
    [6],
    [10]
]

# graph[3].append(12)
# graph[12].append(3)

