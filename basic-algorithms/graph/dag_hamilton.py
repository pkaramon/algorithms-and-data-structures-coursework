def check_if_hamilton_exists(vertices, graph):
    n = len(graph)
    if len(vertices) != n:
        return False

    for i in range(0, n - 1):
        if vertices[i + 1] not in graph[vertices[i]]:
            return False
    return True


def hamilton_dag(graph):
    n = len(graph)
    visited = [False] * n
    output = []
    topo_sort(0, graph, visited, output)
    output.reverse()

    return check_if_hamilton_exists(output, graph), output


def topo_sort(v, graph, visited, output):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            topo_sort(u, graph, visited, output)
    output.append(v)
