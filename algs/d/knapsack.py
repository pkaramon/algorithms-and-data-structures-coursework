import heapq

def knapsack(items, max_weight):
    """
    We need to find the most profitable subset of items such that their overall weight <= max_weight.

    F({a0, ..., ai}, mw) := most profit we get if overall sum of taken items is <= mw

    F({a0, ..., ai}, mw) = max {
        F({a0,..., ai-1}, mw),
        F({a0,..., ai-1}, mw-weight[i]) + value[i] if mw-weight[i] >= 0
    }

    F({}, mw) = 0

    @param items: list [(value, weight)...]
    @param max_weight: maximum weight a thief can carry
    @return:
    """

    n = len(items)

    values = [items[i][0] for i in range(n)]
    weights = [items[i][1] for i in range(n)]

    F = [[-1 for _ in range(max_weight + 1)] for _ in range(n)]
    parent = [False for _ in range(max_weight + 1)]

    for w in range(max_weight + 1):
        F[0][w] = values[0] if weights[0] <= w else 0
    parent[0] = weights[0] <= max_weight

    for i in range(1, n):
        for w in range(max_weight + 1):
            F[i][w] = F[i - 1][w]
            if w - weights[i] >= 0 and F[i - 1][w - weights[i]] + values[i] > F[i][w]:
                F[i][w] = F[i - 1][w - weights[i]] + values[i]

        parent[i] = F[i][max_weight] > F[i - 1][max_weight]

    return F[n - 1][max_weight], reconstruct(items, parent)


def reconstruct(items, parent):
    n = len(items)
    items_taken = []
    for x in range(n - 1, -1, -1):
        if parent[x]:
            items_taken.append(items[x])
    items_taken.reverse()
    return items_taken


def knapsack_2d(items, max_weight, max_height):
    """
    Find the most profitable subset of items.
    Such that their overall weight and height are <= to respectively max_weight and max_height.

    RW := remaining weight
    RH := remaining height

    F([a0, a1, ..., ai], RW, RH) = max(
        F([a0, a1, ..., ai-1], RW-wi, RH-hi) + vi,  if no negatives
        F([a0, a1, ..., ai-1], RW, RH)
    )

    F([a0], RW, RH) = {
        a0 if hi <= RH and wi <= RW
        0 otherwise
    }


    @param items: [(value, weight, height)...]
    @param max_weight: max overall weight of taken items
    @param max_height: max overall height of taken items
    @return:
    """

    n = len(items)

    values = [items[i][0] for i in range(n)]
    weights = [items[i][1] for i in range(n)]
    heights = [items[i][2] for i in range(n)]

    F = [[[-1 for _ in range(max_height + 1)] for _ in range(max_weight + 1)] for _ in range(n)]

    for w in range(max_weight + 1):
        for h in range(max_height + 1):
            F[0][w][h] = values[0] if (weights[0] <= w and heights[0] <= h) else 0

    def inner(i, w, h):
        if i < 0 or w < 0 or h < 0:
            return 0

        if i == 0:
            return values[0] if (weights[0] <= w and heights[0] <= h) else 0

        if F[i][w][h] == -1:
            F[i][w][h] = max(inner(i - 1, w, h), inner(i - 1, w - weights[i], h - heights[i]) + values[i])
        return F[i][w][h]

    res = inner(n - 1, max_weight, max_height)
    import pprint
    pprint.pprint(F)
    return res


def knapsack_2d_v2(items, max_weight, max_height):
    n = len(items)

    values = [items[i][0] for i in range(n)]
    weights = [items[i][1] for i in range(n)]
    heights = [items[i][2] for i in range(n)]

    last_pane = [[values[0] if weights[0] <= w and heights[0] <= h else 0 for h in range(max_height + 1)]
                 for w in range(max_weight + 1)]
    current = [[-1 for _ in range(max_height + 1)] for _ in range(max_weight + 1)]

    for i in range(1, n):
        for w in range(max_weight + 1):
            for h in range(max_height + 1):
                current[w][h] = last_pane[w][h]
                if weights[i] <= w and heights[i] <= h:
                    current[w][h] = max(current[w][h], last_pane[w - weights[i]][h - heights[i]] + values[i])

        current, last_pane = last_pane, current

    return last_pane[max_weight][max_height]


def knapsack_2d_final(items, max_weight, max_height):
    n = len(items)
    values = [items[i][0] for i in range(n)]
    weights = [items[i][1] for i in range(n)]
    heights = [items[i][2] for i in range(n)]

    dp = [[(values[0] if weights[0] <= w and heights[0] <= h else 0) for h in range(max_height + 1)]
          for w in range(max_weight + 1)]
    parent = [False for _ in range(n)]  # parent[i] -> i-th item was taken

    for i in range(1, n):
        last = dp[max_weight][max_height]
        for w in range(max_weight, -1, -1):
            for h in range(max_height, -1, -1):
                if w >= weights[i] and h >= heights[i] and dp[w - weights[i]][h - heights[i]] + values[i] > dp[w][h]:
                    dp[w][h] = dp[w - weights[i]][h - heights[i]] + values[i]
        parent[i] = dp[max_weight][max_height] > last
    return dp[max_weight][max_height], reconstruct(items, parent)


print(
    knapsack([(5, 2)], 2)
)

print(knapsack(
    [(5, 2),
     (8, 3),
     (10, 4),
     (11, 20),
     (3, 1),
     (7, 6)
     ], 10
))

print(knapsack_2d_final(
    items=[(5, 2, 9),
           (8, 3, 6),
           (10, 4, 4),
           (11, 20, 1),
           (3, 1, 1),
           (7, 6, 7)],
    max_height=10,
    max_weight=10
))
#
