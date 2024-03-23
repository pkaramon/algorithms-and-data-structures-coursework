from collections import deque


# graph is represented by a matrix
# by default loops i.e. (u,u) edges are 0
# so are edges which does not exist in the flow graph

def find_max_flow(graph, s, t):
    max_flow = 0
    while (path := find_path(graph, s, t)) is not None:
        min_weight = min_path_weight(graph, path)
        max_flow += min_weight
        update_weights(graph, path)
    return max_flow


def create_path_from_parent(parent, s, t):
    path = []
    v = t
    while v != parent[s]:
        path.append(v)
        v = parent[v]
    path.reverse()
    return path


def find_path(graph, s, t):
    n = len(graph)
    q = deque()
    visited = [False] * n
    parent = [None] * n

    visited[s] = True
    q.append(s)

    while len(q) > 0:
        v = q.popleft()
        if v == t:
            return create_path_from_parent(parent, s, t)
        for u in range(n):
            if graph[v][u] > 0 and not visited[u]:
                visited[u] = True
                parent[u] = v
                q.append(u)
    return None


def min_path_weight(graph, path):
    min_weight = float('inf')
    for i in range(1, len(path)):
        min_weight = min(min_weight, graph[path[i - 1]][path[i]])
    return min_weight


def update_weights(graph, path):
    min_weight = min_path_weight(graph, path)
    for i in range(1, len(path)):
        v, u = path[i - 1], path[i]
        graph[v][u] -= min_weight
        graph[u][v] += min_weight


def from_list_of_edges(n, edges):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for u, v, w in edges:
        graph[u][v] = w
    return graph


g = from_list_of_edges(6,
                       [(0, 1, 4),
                        (0, 3, 3),
                        (1, 2, 2),
                        (1, 3, 2),
                        (2, 5, 4),
                        (3, 2, 2),
                        (3, 4, 2),
                        (4, 5, 5)])

print(find_max_flow(g, 0, 5))
