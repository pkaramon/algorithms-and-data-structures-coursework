""" Piotr Karamon
"""


def ksum(T, k, p):
    n = len(T)
    total = 0

    A = [(T[i], i) for i in range(n)]
    A.sort()
    print(A)
    print(list(sorted(T)))

    return total


print(ksum([7, 9, 1, 5, 8, 6, 2, 12], 4, 5))
