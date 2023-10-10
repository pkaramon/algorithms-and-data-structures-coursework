""" Piotr Karamon
Brute force. algorytm sortuje tablice krawędzi.
Następnie analizuje możliwe wartości m i M i tworzy na ich podstawie drzewo rozpinające.
Sprawdzjąc jednocześnie czy spełnia ono warunki zadania.

Czas: O(E^2*E*logV)

"""
from kol2testy import runtests


def beautree(G):
    # tu prosze wpisac wlasna implementacje
    n = len(G)

    edge_list = []
    for v in range(n):
        for u, w in G[v]:
            if v < u:
                edge_list.append((v, u, w))

    edge_list.sort(key=lambda e: e[2])
    result = float('inf')

    for m_i in range(0, len(edge_list)):
        for M_i in range(m_i + 1, len(edge_list)):
            s_weights, ok = find_st(edge_list, n, m_i, M_i)
            if ok:
                result = min(s_weights, result)
    return result if result != float('inf') else None


class Node:
    def __init__(self):
        self.rank = 0
        self.parent = self


def find_st(edge_list, n, m_i, M_i):
    nodes = [Node() for _ in range(n)]
    in_set = [False] * n
    edge_sum = 0

    m, M = edge_list[m_i][2], edge_list[M_i][2]

    mst_edges = [False] * len(edge_list)

    for i in range(m_i, M_i+1):
        v, u, w = edge_list[i]
        if m <= w <= M and find_set(nodes[v]) is not find_set(nodes[u]):
            union(nodes[v], nodes[u])
            in_set[u] = True
            in_set[v] = True
            mst_edges[i] = True
            edge_sum += w

    for i in range(len(mst_edges)):
        if not mst_edges[i]:
            if m <= edge_list[i][2] <= M:
                return edge_sum, False

    return edge_sum, all(in_set)


def find_set(x):
    if x.parent != x:
        x.parent = find_set(x.parent)
    return x.parent


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(beautree, all_tests=True)
