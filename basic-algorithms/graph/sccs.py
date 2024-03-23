def driver(graph):
    n = len(graph)
    processed = []
    visited = [False for _ in range(n)]

    for v in range(n):
        if not visited[v]:
            dfs_visit(v, graph, visited, processed)

    sccs = get_sccs(graph, processed)
    scc_ids = [-1] * n
    for i, scc in enumerate(sccs):
        for v in scc:
            scc_ids[v] = i

    scc_graph = create_scc_graph(graph, scc_ids, sccs)


def get_sccs(graph, processed):
    n = len(graph)
    visited = [False for _ in range(n)]
    sccs = []
    transpose = create_transpose_graph(graph)
    for v in reversed(processed):
        if not visited[v]:
            scc = []
            dfs_visit(v, transpose, visited, scc)
            sccs.append(scc)
    return sccs


def create_scc_graph(graph, scc_ids, sccs):
    n = len(graph)
    for i, scc in enumerate(sccs):
        for v in scc:
            scc_ids[v] = i
    scc_graph = [[] for _ in range(len(sccs))]
    for v in range(n):
        for u in graph[v]:
            if scc_ids[v] != scc_ids[u]:
                scc_graph[scc_ids[v]].append(scc_ids[u])
    return scc_graph


def dfs_visit(v, graph, visited, output):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs_visit(u, graph, visited, output)
    output.append(v)


def create_transpose_graph(graph):
    n = len(graph)
    transpose = [[] for _ in range(n)]
    for v in range(n):
        for u in graph[v]:
            transpose[u].append(v)
    return transpose
