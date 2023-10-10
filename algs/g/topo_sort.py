def topo_sort(v, graph, visited, output):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            topo_sort(u, graph, visited, output)
    output.append(v)
