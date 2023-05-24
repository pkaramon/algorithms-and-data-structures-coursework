class Node:
    def __init__(self, value):
        self.parent = self
        self.rank = 0
        self.value = value


def findset(x: Node):
    if x.parent != x:
        x.parent = findset(x.parent)
    return x.parent


def union(x, y):
    x = findset(x)
    y = findset(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal(graph):
    n = ...
    edges = ...
    edges.sort(key=lambda e: graph[e[0]][e[1]])
    mst = []
    vertices = [Node(i) for i in range(n)]

    for u,v in edges:
        if findset(vertices[u]) is not findset(vertices[v]):
            mst.append((u, v))
            union(vertices[u], vertices[v])

    return mst
