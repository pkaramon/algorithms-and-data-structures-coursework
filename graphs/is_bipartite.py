def try_to_color(graph, vertex, colors):
    for neighbour in graph[vertex]:
        if colors[neighbour] == colors[vertex]:
            return False
        if colors[neighbour] != 0:
            continue
        colors[neighbour] = -colors[vertex]

        if not try_to_color(graph, neighbour, colors):
            return False
    return True


def is_bipartite(graph):
    """graph is a list of lists of neighbours"""
    order = len(graph)
    colors = [0] * order

    for v in range(order):
        if colors[v] == 0:
            colors[v] = 1
            if not try_to_color(graph, v, colors):
                return False
    return True


def is_bipartite_v2(graph: list[list[int]]):
    order = len(graph)
    visited = [False] * order
    colors = [0] * order

    def try_coloring(vertex):
        for neighbour in graph[vertex]:
            if colors[vertex] == colors[neighbour]:
                return False
            if visited[neighbour]:
                continue
            colors[neighbour] = -colors[vertex]
            visited[neighbour] = True
            if not try_coloring(neighbour):
                return False
        return True

    for v in range(order):
        if not visited[v]:
            visited[v] = True
            colors[v] = 1
            if not try_coloring(v):
                return False
    return True
