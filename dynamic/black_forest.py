def black_forest(wood):
    """
    We need to find the most effective way of cutting down the trees(get the most wood).
    There is one condition -> we cannot cut down trees that are next to each other.

    F(i, true) := maximum amount of wood we can get from 0..i trees if we cut the i-th tree
    F(i, false) := analogous

    F(i, true) = F(i-1, false) + wood[i]
    F(i, false) = max(F(i-1, false), F(i-1, true))

    @param wood: list of amounts of wood
    @return:
    """
    n = len(wood)

    cut = [0 for _ in range(n)]
    not_cut = [0 for _ in range(n)]
    parent = [None for _ in range(n)]

    for i in range(1, n):
        cut[i] = not_cut[i-1] + wood[i]
        not_cut[i] = max(not_cut[i-1], cut[i-1])

    trees_cut = [(wood[i], i) for i in range(n) if cut[i] > not_cut[i]]

    return max(cut[n-1], not_cut[n-1]), trees_cut

print(black_forest([1,3,2,4,5,8]))
