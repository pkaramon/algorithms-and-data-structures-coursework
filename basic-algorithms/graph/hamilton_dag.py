"""
Algorithm:
We do topology sort.
And get the following list v1 v2 v3 v4 ... vn
where edges only go from right to left.

Claim: Hamiltonian path exists <=> for every vi v(i+1) there exist (vi, v(i+1)) in edges.

<= Trivial. This gives a way of obtaining a path which is Hamiltonian

=> Because if (vi, v(i+1)) does not exist in edges
   then after we "jump" there is NO WAY to get v(i+1) into the path.
   Meaning it won't be Hamiltonian.
"""


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


graph = [
    [1, 4],
    [2],
    [5, 3],
    [5],
    [1, 5, 6],
    [6],
    [],
]
print(hamilton_dag(graph))
