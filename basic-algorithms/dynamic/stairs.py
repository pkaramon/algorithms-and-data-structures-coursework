def stairs(n, k):
    F = [-1] * (n + 1)
    F[0] = 1

    for i in range(1, n + 1):
        total = 0
        for j in range(max(i - k, 0), i):
            total += F[j]
        F[i] = total
    return F[n]


def stairs_optim(n, k):
    last = [0] * k
    last[0] = 1

    for i in range(1, k):
        last[i] = sum(last[j] for j in range(0, i))

    for i in range(n - k + 1):
        temp = last[1:]
        last[k - 1] = sum(last)
        last[0:k - 1] = temp

    return last[k - 1]


def stairs_optim_better(n, k):
    F = [-1] * k
    F[0] = 1

    for i in range(1, n + 1):
        total = 0
        for j in range(max(i - k, 0), i):
            total += F[(i - j) % k]

        F[i] = total
    return F[n % k]


def stairs_red(n, k, red_stairs):
    """
    @param n: which step to calculate
    @param k: how many steps are we allowed to take at a time
    @param red_stairs: bool array indicating whether i-th step is red
    @return: number of numbers to get to the i-th step by skipping red stairs
    """

    F = [-1] * (n + 1)
    F[0] = 1

    for i in range(1, n + 1):
        total = 0
        for j in range(max(i - k, 0), i):
            if not red_stairs[j]:
                total += F[j]
        F[i] = total
    return F[n]


def stairs_paid(n, prices):
    min_cost = [float('inf')] * (n + 1)
    min_cost[0] = 0
    min_cost[1] = prices[1]

    parent = [None] * (n + 1)

    for i in range(2, n + 1):
        if prices[i - 1] < prices[i - 2]:
            min_cost[i] = prices[i] + prices[i - 1]
            parent[i] = i - 1
        else:
            min_cost[i] = prices[i] + prices[i - 2]
            parent[i] = i - 2

    return min_cost[n], from_parent_to_items(parent, n)


def from_parent_to_items(parent, last):
    x = last
    items = []
    while x is not None:
        items.append(x)
        x = parent[x]
    items.reverse()
    return items


print(stairs_paid(4, [1, 3, 2, 8, 1]))
print(stairs_optim(20, 7))
print(stairs(20, 7))
# print(stairs_optim_better(20, 7))
