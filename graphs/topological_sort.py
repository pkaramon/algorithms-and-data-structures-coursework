# def topological_sort(graph):
#     for


def dfs(graph):
    n = len(graph)
    visited = [False] * n
    parent = [None] * n

    time = 0

    def dfs_visit(graph, v, visited, parent):
        nonlocal time
        time += 1
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                parent[u] = v
                dfs_visit(graph, u, visited, parent)

    for v in range(n):
        if not visited[v]:
            dfs_visit(graph, v, visited, parent)


def topological_sort(graph):
    n = len(graph)
    visited = [False] * n
    order = []
    for v in range(n):
        if not visited[v]:
            dfs_visit(graph, v, visited, order)
    order.reverse()
    return order


def dfs_visit(graph, v, visited, order):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs_visit(graph, u, visited, order)
    order.append(v)


graph = [
    [1, 2],  # 0
    [2, 3],  # 1
    [],  # 2
    [4, 5],  # 3
    [],  # 4
    [],  # 5
    [3]  # 6
]
print(topological_sort(graph))
