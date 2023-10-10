def floyd_warshall(graph):
    n = len(graph)
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    parent = [[None for _ in range(n)] for _ in range(n)]

    for v in range(n):
        for u in range(n):
            if graph[v][u] < float('inf'):
                parent[v][u] = v

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][i]:
                    dist[i][j] = dist[i][k] + dist[k][i]
                    parent[i][j] = parent[k][j]
