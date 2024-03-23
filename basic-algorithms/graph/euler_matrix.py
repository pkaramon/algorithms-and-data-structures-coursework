def euler_matrix_undirected(matrix):
    order = len(matrix)
    edge_indexes = [0] * order
    cycle = []

    def dfs_visit(v):
        for u in range(edge_indexes[v], order):
            edge_indexes[v] += 1
            if matrix[v][u]:
                matrix[v][u] = 0
                matrix[u][v] = 0  # omit if graph is directed
                dfs_visit(u)
        cycle.append(v)

    dfs_visit(0)
    return cycle[::-1]
