def from_matrix_to_adj(matrix):
    n = len(matrix)
    g = [[] for _ in range(n)]
    for v in range(n):
        for u in range(n):
            if matrix[v][u] != 0:
                g[v].append((u, matrix[v][u]))
    return g

def from_edges_to_adj_list(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


