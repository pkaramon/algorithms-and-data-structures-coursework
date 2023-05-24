def n_components(graph):
    order = len(graph)
    visited = [False] * order

    def dfs_visit(v):
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                dfs_visit(u)

    n = 0
    for v in range(order):
        if not visited[v]:
            dfs_visit(v)
            n += 1
    return n


def get_components(graph):
    order = len(graph)
    visited = [False] * order
    comp_ids = [-1] * order

    def dfs_visit(v, comp_id):
        visited[v] = True
        comp_ids[v] = comp_id
        for u in graph[v]:
            if not visited[u]:
                dfs_visit(u, comp_id)

    comp_id = 0
    for v in range(order):
        if not visited[v]:
            dfs_visit(v, comp_id)
            comp_id += 1
    return comp_ids, get_components_from_ids(comp_id, comp_ids)


def get_components_from_ids(n, comp_ids):
    components = [[] for _ in range(n)]
    for i in range(len(comp_ids)):
        components[comp_ids[i]].append(i)
    return components


graph_map = {
    0: [5],
    1: [5, 6],
    2: [5, 6, 7],
    3: [5, 7],
    4: [],
    5: [0, 1, 2, 3, ],
    6: [1, 2, ],
    7: [2, 3, ],
    8: [9, 10],
    9: [8],
    10: [8],
    11: [],
}

graph = [0] * len(graph_map)
for i in range(len(graph_map)):
    graph[i] = graph_map[i]

print(n_components(graph))
print(get_components(graph))
