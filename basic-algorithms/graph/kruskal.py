class Node:
    def __init__(self):
        self.parent = self
        self.rank = 0


def find_set(x):
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


def union(x, y):
    x, y = find_set(x), find_set(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal(graph):
    n = len(graph)
    edges = []
    for v in range(n):
        for u, w in graph[v]:
            if v < u:
                edges.append((v, u, w))

    edges.sort(key=lambda e: e[2])

    mst_edges = []
    nodes = [Node() for _ in range(n)]

    for v, u, w in edges:
        if find_set(nodes[v]) is not find_set(nodes[u]):
            mst_edges.append((v, u, w))
            union(nodes[v], nodes[u])
    return mst_edges
