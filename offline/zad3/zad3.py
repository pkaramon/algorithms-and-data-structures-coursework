"""Piotr Karamon

Algorytm sortuje najpierw tablicę quick sortem. Następnie przechodzimy przez nią
i zliczamy ile razy dany string wystąpił. Kolejno szukamy połówkowo w tablicy
odwrotności naszego obecnego stringa i zliczamy ile takich jest(no chyba że jest
palindromem to wtedy nie). Po tych wszystkich krokach mamy siłę naszego napisu i
porównujemy ją z obecnie największą siłą.

czas  : O(N + nlogn)
pamięć: O(logn)
"""
from zad3testy import runtests

def strong_string(T):
    n = len(T)
    if n == 0:
        return 0

    quick_sort(T, 0, n-1)

    max_strength = 0
    i = 0
    while i < n:
        curr_strength = 1
        j = i + 1

        while j < n and T[j] == T[i]:
            curr_strength += 1
            j += 1

        rev = T[i][::-1]

        if rev != T[i]:
            rev_start = binary_search(T, rev, j)
            k = rev_start
            while 0 <= k < n and T[k] == rev:
                curr_strength += 1
                k += 1

            k = rev_start-1
            while 0 <= k and T[k] == rev:
                curr_strength += 1
                k -= 1

        max_strength = max(max_strength, curr_strength)
        i = j

    return max_strength


R_SEED = 7
R_A = 134775813
R_C = 1
R_MODULUS = 2**32


def rand():
    global R_SEED
    R_SEED = (R_A * R_SEED + R_C) % R_MODULUS
    return R_SEED


def partition(T, left, right):
    pivot_ind = rand() % (right-left+1) + left
    T[right], T[pivot_ind] = T[pivot_ind], T[right]

    pivot = T[right]

    i = left - 1
    for j in range(left, right):
        if T[j] < pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[right] = T[right], T[i+1]
    return i+1


def quick_sort(T, left, right):
    while left < right:
        q = partition(T, left, right)
        quick_sort(T, left, q-1)
        left = q+1


def binary_search(array, x, low=0):
    high = len(array) - 1
    while low <= high:
        m = (low+high) // 2
        if x == array[m]:
            return m
        elif x < array[m]:
            high = m - 1
        else:
            low = m+1
    return -1


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests(strong_string, all_tests=True)
