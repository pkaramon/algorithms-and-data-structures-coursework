def floyd_warshall(graph):
    """
    does shit
    @param graph: matrix
    @return:
    """
    n = len(graph)
    dist = [[graph[v][u] for u in range(n)] * n for v in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for v in range(n):
            for u in range(n):
                dist[v][u] = min(dist[v][u], dist[v][k] + dist[k][u])
