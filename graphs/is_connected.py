def is_connected(graph):
    order = len(graph)
    visited = [False] * order

    def dfs_visit(v):
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                dfs_visit(u)

    dfs_visit(0)
    return all(visited)


graph = [
    [1, 2, 3, 6],
    [5, 2],
    [0, 4],
    [4, 5],
    [2, 5],
    [],
    [1],
    [],

]

print(is_connected(graph))
