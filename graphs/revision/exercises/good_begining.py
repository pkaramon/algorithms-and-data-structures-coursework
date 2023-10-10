"""
Brute force:
Run DFS/BFS from every vertex and check if all other vertices were visited.
Time: O((V+E)*V)

Smarter:
Find SCCs and then topologically sort the SCC graph.
In the topologically first SCC there is our good beginning.

"""


def find_good_beginning_in_dag(graph):
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

    # there are duplicate edges in this edges
    # I know that and don't care
    scc_graph = create_scc_graph(graph, scc_ids, sccs)
    topo_sorted = []
    dfs_visit(0, scc_graph, [False] * len(scc_graph), topo_sorted)
    topo_sorted.reverse()

    for v in range(n):
        if scc_ids[v] == topo_sorted[0]:
            return True, v


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


def dfs_visit(v, graph, visited, output):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs_visit(u, graph, visited, output)
    output.append(v)


def dfs_scc_graph(v, graph, visited, scc_ids, scc_graph):
    visited[v] = True
    for u in graph[v]:
        if not visited[u] and scc_ids[u] != scc_ids[v]:
            scc_graph[scc_ids[v]].append(scc_ids[u])
        if not visited[u]:
            dfs_scc_graph(u, graph, visited, scc_ids, scc_graph)


def create_transpose_graph(graph):
    n = len(graph)
    transpose = [[] for _ in range(n)]
    for v in range(n):
        for u in graph[v]:
            transpose[u].append(v)
    return transpose


g = [
    'b',
    'ci',
    'ad',
    'eg',
    'f',
    'd',
    'f',
    'i',
    'j',
    'kf',
    'dh',
]

g = [
    [ord(c) - ord('a') for c in list(neighbours)]
    for neighbours in g
]

find_good_beginning_in_dag(g)
