def find_bridges(graph):
    n = len(graph)
    low = [float('inf')] * n
    time = 0
    times = [None] * n

    bridges = []

    def dfs_visit(v, parent):
        nonlocal time
        time += 1

        times[v] = time
        low[v] = min(low[v], times[v])

        for u in range(n):
            if u != parent and graph[v][u] and times[u] is not None:
                low[v] = min(low[v], times[u])

            if graph[v][u] and times[u] is None:
                dfs_visit(u, v)
                low[v] = min(low[v], low[u])

        if low[v] == times[v] and parent is not None:
            bridges.append((parent, v))

    dfs_visit(0, None)
    return bridges
