class FUSet:
    ...


def union_set(s1, s2):
    ...


def find_set(s1, s2):
    ...


# edges = [(i, j, waga), ...]
def travel_agency(n, edges, turists, a, b):
    edges = edges.sort(key=lambda e: -e[2])
    sets = [FUSet() for _ in range(n)]
    mst = []

    for v, u, w in edges:
        if find_set(sets[v]) != find_set(sets[u]):
            mst.append((v, u, w))
            union_set(sets[u], sets[v])

        if find_set(sets[a]) == find_set(sets[b]):
            print
