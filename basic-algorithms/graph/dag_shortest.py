# toposort, for every v in topo_sorted: relax edges from v

def dag_shortest(graph):
    n = len(graph)
    ordering = []
    visited = [False] * n
    dfs_topo_sort(0, graph, visited, ordering)
    ordering.reverse()
    print(ordering)

    d = [float('inf')] * n
    parent = [None] * n
    d[ordering[0]] = 0

    for v in ordering:
        for u, w in graph[v]:
            if w + d[v] < d[u]:
                parent[u] = v
                d[u] = w + d[v]
    return parent, d


def dfs_topo_sort(v, graph, visited, ordering):
    visited[v] = True
    for u, w in graph[v]:
        if not visited[u]:
            dfs_topo_sort(u, graph, visited, ordering)
    ordering.append(v)


"a 0" \
" b 1" \
" c 2" \
" d 3" \
" e 4" \
" f 5" \
" g 6" \
" h 7"

graph = [
    [(1, 3), (2, 6)],
    [(2, 4), (4, 11), (3, 4)],
    [(3, 8), (6, 11), ],
    [(4, -4), (5, 5), (6, 2), ],
    [(7, 9)],
    [(7, 1)],
    [(7, 2)],
    []
]

print(dag_shortest(graph))
