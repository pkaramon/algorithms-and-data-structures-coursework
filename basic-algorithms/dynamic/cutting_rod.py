# prices = [1, 5, 8, ...]


def cut_rod(n, prices):
    """
    f(i) - maximum profit we can get by cutting i-th length rod

    f(i) = max {
        f(i-k) + price(k) for k in range(1,i)
    }

    @param prices: [(3, 2), (4, 3)] for 3 length we get 2 for 4 length we get 3
    @return: max profit
    """

    P = [0 for _ in range(n + 1)]
    for length, price in prices:
        P[length] = price

    f = [P[length] for length in range(n + 1)]

    for i in range(n + 1):
        for k in range(i // 2 + 1):
            f[i] = max(f[i], f[i - k] + f[k])
    return f[n]


def cutting_rod(prices):
    n = len(prices)
    max_prices = [0] * (n + 1)
    return max_price(max_prices, prices, n)


def max_price(max_prices, prices, k):
    if max_prices[k] != 0:
        return max_prices[k]

    max_prices[k] = max(
        (max_price(max_prices, prices, i) + max_price(max_prices, prices, k - i)
         for i in range(1, k)),
        default=0
    )
    max_prices[k] = max(max_prices[k], prices[k - 1])
    return max_prices[k]


print(cutting_rod([3, 5, 8, 9, 10, 17, 17, 20]))
print(cut_rod(8, [(1, 3), (2, 5), (3, 8), (4, 9), (5, 10), (6, 17), (7, 17), (8, 20)]))
