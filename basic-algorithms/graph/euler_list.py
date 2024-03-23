class RemovedIndicator:
    def __init__(self):
        self.removed = False

    def __repr__(self):
        return f'{self.removed}'


def transform_adj_list(graph):
    n = len(graph)
    transformed = [[] for _ in range(n)]
    for v in range(n):
        for u in graph[v]:
            if v < u:
                indicator = RemovedIndicator()
                transformed[u].append((v, indicator))
                transformed[v].append((u, indicator))
    return transformed


def find_euler_cycle(graph):
    graph = transform_adj_list(graph)
    n = len(graph)
    edge_indexes = [0 for _ in range(n)]
    processed = [False for _ in range(n)]
    cycle = []

    def dfs_visit(v):
        for i in range(edge_indexes[v], len(graph[v])):
            u, indicator = graph[v][i]
            edge_indexes[v] += 1
            if not processed[u] and not indicator.removed:
                indicator.removed = True
                dfs_visit(u)
        processed[v] = True
        cycle.append(v)

    dfs_visit(0)
    return cycle[::-1]
