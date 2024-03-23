"""graph is a matrix"""
from graphs.revision.utils import from_edges_to_adj_list


def telecom(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    deletion_order = []
    dfs_visit(0, graph, visited, parent, deletion_order)
    print(deletion_order)
    print(parent)
    print(create_dfs_tree(parent))


def create_dfs_tree(parent):
    n = len(parent)
    tree = [[] for _ in range(n)]
    for v in range(1, n):
        tree[parent[v]].append(v)
    return tree


def dfs_visit(v, graph, visited, parent, deletion_order):
    print('visisted', v)
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            parent[u] = v
            dfs_visit(u, graph, visited, parent, deletion_order)
    deletion_order.append(v)


graph = from_edges_to_adj_list(11, [
    (0, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 6),
    (4, 5),
    (5, 6),
    (5, 7),
    (7, 9),
    (7, 8),
    (8, 10),
    (9, 10),
])

telecom(graph)
