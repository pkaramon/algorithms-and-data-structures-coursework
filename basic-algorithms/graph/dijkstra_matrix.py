def dijkstra(M, s):
    # diagonal - zeros
    n = len(M)
    dist = [float('inf')] * n
    visited = [False] * n
    parent = [None] * n

    dist[s] = 0
    visited[s] = True

    while True:
        min_dist, ind = float('inf'), -1
        for i in range(n):
            if dist[i] < min_dist and not visited[i]:
                min_dist, ind = dist[i], i
        if ind == -1:
            return dist

        visited[ind] = True
        for v in range(n):
            if dist[v] > dist[ind] + M[ind][v]:
                dist[v] = dist[ind] + M[ind][v]
                parent[v] = ind
