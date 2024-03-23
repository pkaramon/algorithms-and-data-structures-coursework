def fib(n):
    if n <= 1: return 1

    F = [-1] * (n + 1)
    F[0] = F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]


# f(i) -> length of the longest rising subsequence ending at i-th element
# f(0) = 1
# f(i) =
#       max(
#          f(j) + 1, A[j] < A[i+1]
#       )

def lis(numbers):
    n = len(numbers)
    lengths = [1] * n
    parent = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if numbers[j] < numbers[i] and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
                parent[i] = j

    max_i = 0
    for i, val in enumerate(lengths):
        if lengths[val] > lengths[max_i]:
            max_i = i

    return lengths[max_i], max_i, from_parent(max_i, parent, numbers)


def from_parent(i, parent, numbers):
    nums = []
    while i != -1:
        nums.append(numbers[i])
        i = parent[i]
    nums.reverse()
    return nums


class Employee:
    def __init__(self, fun):
        self.emp = []
        self.fun = fun
        self.best_party = -1
        self.without_me = -1


def best_party(p):
    if p.best_party >= 0:
        return p.best_party

    p.best_party = max(
        sum(without_me(e) for e in p.emp) + p.fun,
        without_me(p),
    )
    return p.best_party


def without_me(p):
    if p.without_me >= 0:
        return p.without_me
    p.without_me = sum(best_party(e) for e in p.emp)
    return p.without_me


# items = [(price, weight) ...]
# f(i, b) -> maximum price of items {0, ..., i},
#            under the condition that their total weight < b
def knapsack(W, P, B):
    n = len(W)
    F = [[0 for b in range(B + 1)] for i in range(n)]

    for b in range(W[0], B + 1):
        F[0][b] = P[0] if W[0] <= B else 0

    for b in range(B + 1):
        for i in range(1, n):
            F[i][b] = F[i - 1][b]
            if b >= W[i]:
                F[i][b] = max(F[i][b], F[i - 1][b - W[i]] + P[i])
    return F[n - 1][B]


def max_price(max_prices, items, i, b):
    if i == 0:
        return -1 if items[i] > b else items[i]

    return max(
        max_price(items, i - 1, b),
        max_price(items, i - 1, b - items[i][1]) + items[i][0]
    )


print(lis([1, 3, 5, 2, 1, 3, 5, 7]))
