from copy import deepcopy
from math import inf


def update_weights(G, path):
    w = min_weight(G, path)
    for i in range(1, len(path)):
        u, v = path[i - 1], path[i]
        G[u][v] -= w
        G[v][u] += w


def ford_fulkerson(M, s, t):
    n = len(M)
    G = deepcopy(M)
    my_path = find_path(G, s, t)
    count = 0
    while my_path:
        count += min_weight(G, my_path)
        update_weights(G, my_path)
        my_path = find_path(G, s, t)
    return count, G


def find_path(G, s, t):
    """
    @return: list of vertices
    """
    ...


def min_weight(G, my_path):
    min_w = inf
    for i in range(1, len(my_path)):
        min_w = min(min_w, G[my_path[i - 1]][my_path[i]])
    return min_w


# graf nieskierowany przerabiamy na skierowany
# sieć fabryka każda fabryka produkuje rzeczy w kontenerach są sklepy
# kontenery są tranposortowane koleją
# kilka źródeł i kilka ujść
# fabryka 1 mozę wyprodukować 70
# fabryka 2 mozę wyprodukować 3
# sklep 1 może przyjąć 5
# sklep 2 może przyjąć 10
# ...
# tworzymy jedno żródło i jedno ujście
# i krawędzie z jednego źródła do pierwotnych źródłem
# mają wagi równe "efektywności" fabyryk
# jeżeli brak ograniczeń -> suma wag w grafie albo inf


def railway(M, factories, stores):
    """
    @param M: matrix repr
    @param factories: list of tuples (vertex index, max flow out)
    @param stores: list of tuples (vertex index, max flow in)
    @return: ...
    """

    G = deepcopy(M)
    n = len(M)

    for row in G:
        row.extend([0, 0])

    main_factory, main_store = n, n + 1
    G.append([0] * (n + 2))
    G.append([0] * (n + 2))

    for v, max_flow in factories:
        G[main_factory][v] = max_flow

    for v, max_flow in stores:
        G[v][main_store] = max_flow

    return ford_fulkerson(G, main_factory, main_store)
    # normal ford fulkerson

# graf nieskierowany i nieważony
# ile krawędzi minimalnie usunąć żeby go rozpójnić
# spójność krawędziowa(G) = k iff gdy usuniemy k-1 to graf się nie rozpójni
# a gdy usuniemy odpowiednie k to się rozpójni

# max skojarzenie w grafie dwudzielnym, drzewie
