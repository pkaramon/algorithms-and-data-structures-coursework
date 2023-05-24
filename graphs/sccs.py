"""

A graph is said to be strongly connected if every
vertex is reachable from every other vertex.
Strongly connected components of a graph
form a partition into sub-graphs that are themselves strongly connected.

Graph of SCCs is a directed acyclic graph.
Because if there was a cycle
that means that SCCs belonging to it ought to be
a one big SCC.

Lemma1: If you reverse the edges in the SCC
       that subgraph is still and SCC.

Lemma2: If a subgraph was not an SCC reversing its edges
       won't make it an SCC.

Algorithm:
1. Run first dfs, when a vertex is processed add it on to the stack.
2. Reverse the edges.
3. Pop the first item from the stack and run dfs.
   The vertices that we will encounter in this traversal
   are the first SCC.

   Continue til there are items on the stack.
   (Also have a visited array as in the default DFS).


Graph is represented as an adjacency "matrix".
"""


def create_graph_of_sccs(graph, sccs):
    n = len(graph)
    roots = [-1] * n
    for i, scc in enumerate(sccs):
        for v in scc:
            roots[v] = i

    graph_sccs = [[] for _ in range(len(sccs))]

    for v in range(n):
        for u in graph[v]:
            root_v, root_u = roots[v], roots[u]
            if root_v != root_u:
                graph_sccs[root_v].append(root_u)
    print(roots[2], roots[3])
    return graph_sccs


def get_sccs(graph):
    n = len(graph)
    visited = [False] * n
    processed = []

    for v in range(n):
        if not visited[v]:
            dfs_visit(v, graph, visited, processed)

    sccs = []
    visited = [False] * n
    transpose = create_transpose_graph(graph)
    while len(processed) > 0:
        v = processed.pop()
        if not visited[v]:
            scc = []
            dfs_visit(v, transpose, visited, scc)
            sccs.append(scc)
    return sccs


def dfs_visit(v, graph, visited, processed):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs_visit(u, graph, visited, processed)
    processed.append(v)


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
    'adh',
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

sccs = get_sccs(g)
print(sccs)
print(create_graph_of_sccs(g, sccs))
