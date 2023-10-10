import math


def subset_sum(numbers, total):
    """
    Determine if there exists a subset of A
    such that the sum of the elements is equal to total.

    F(i, total) := can we select a subset from elements 0..i such that their sum = total

    F(i, total) =
        F(i-1, total - numbers[i]), if total - numbers[i] >= 0
        or
        F(i-1, total)

    F(0, total) = numbers[0] == total
    """
    n = len(numbers)
    F = [[False for _ in range(total+1)] for _ in range(n)]
    F[0] = [numbers[0] == t for t in range(total + 1)]
    for i in range(n):
        F[i][0] = True


    for i in range(1, n):
        for t in range(total+1):
            F[i][t] = F[i-1][t]
            if total - numbers[i] >= 0:
                F[i][t] = F[i][t] or F[i-1][t-numbers[i]]

    return F[n-1][total]

