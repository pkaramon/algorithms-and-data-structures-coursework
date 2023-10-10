def dfs(graph):
    order = len(graph)
    visited = [False] * order
    parent = [None] * order
    time = 0

    def dfs_visit(v):
        nonlocal time
        time += 1
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                parent[u] = v
                dfs_visit(u)
        time += 1

    for v in range(order):
        if not visited[v]:
            dfs_visit(v)
