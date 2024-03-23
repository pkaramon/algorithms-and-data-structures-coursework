import math


def my_coin_change(coins, amount):
    """

    F(a) := the minimum number of coins to get amount a
    F(0) = 0
    F(a) = min{F(a-coin) + 1 for coin in coins if a-coin >= 0}

    @param coins: sorted list of available coins
    @param amount: amount to get
    @return: minimum number of coins to get
    """
    F = [math.inf for _ in range(amount + 1)]
    F[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if amount - coin >= 0:
                F[i] = min(F[i], F[i - coin])
            else:
                break
        F[i] += 1

    return F[amount]


def coin_change(coins, amount):
    """
    F(coins_subset, amount) := minimum number of coins from coins_subset to get amount

    F(coins_subset={..., c}, amount) = min{
        F(coins_subset={...}, amount),
        F(coins_subset={..., c}, amount-c)+1 only if amount-c >= 0
     }

     example:
     F({1,3,4,5}, 7) = min{F({1,3,4}, 7), F({1,3,4,5}, 7)}
     F({1,3,4}, 7) = min(F({1,3}, 7), F({1,3}, 3))
     ...

     note: coins_subset is just selection a part of the coins array
     F(i, amount) := minimum of coins to get amount if we only use coins T[:i+1]
     F(i, t) = min(F(i-1, t), F(i, t-coins[i])+1 if t-coins[i]>=0)

    @param coins: coin values in ascending order
    @param amount: amount to get
    @return:
    """

    n = len(coins)
    F = [[math.inf for _ in range(amount + 1)] for _ in range(n)]

    for i in range(n):
        F[i][0] = 0

    for i in range(n):
        for a in range(1, amount + 1):
            F[i][a] = F[i - 1][a]
            if a - coins[i] >= 0:
                F[i][a] = min(F[i][a], F[i][a - coins[i]] + 1)
    return F[n - 1][amount]


print(my_coin_change([1, 3, 4, 7, 13, 15, 17], 123321))
print(coin_change([1, 3, 4, 7, 13, 15, 17], 123321))
