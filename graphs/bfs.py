from collections import deque


# graph is a list of lists of neighbours
def bfs(graph, start_vertex):
    order = len(graph)
    visited = [False] * order
    parent = [None] * order
    distance = [-1] * order

    queue = deque()
    queue.append(start_vertex)
    visited[start_vertex] = True
    distance[start_vertex] = 0

    while len(queue) != 0:
        v = queue.popleft()
        for u in graph[v]:
            if not visited[u]:
                parent[u] = v
                distance[u] = distance[v] + 1
                visited[u] = True
                queue.append(u)

    return visited, parent, distance


graph = [
    [1, 2],
    [2, 4, 3],
    [4],
    [5, ],
    [5],
    [4],
    [7, 8],
    [6, 8],
    [6, 7]
]

print(bfs(graph, 6))
