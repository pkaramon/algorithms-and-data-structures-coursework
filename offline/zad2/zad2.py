""" Piotr Karamon

Największa ilość śniegu jaką można by zebrać to TS = M1 + (M2 -1) + (M3 - 2) + ... + (Mk - (k-1))
Gdzie M1 to największy obszar śniegu, M2 drugi największy itd, i Mk -(k-1) > 0.
Zawsze możemy zebrać właśnie tą największą ilość śniegu.
Wynika to z faktu iż całkowita wartość zebranego śniegu nie zależy od kolejności
zbierania tego śniegu(o ile zbierając jakiś śnieg Mi nie zniszczymy jakiegoś Mj).

Algorytm sortuje tablicę S quick sortem by uzyskać wartość TS, w momencie w którym
wiadomo że już więcej śniegu nie uda się zebrać kończy sortowanie.

Złożoność czasowa    : O(nlogn)
Złożoność pamięciowa : O(n)
"""

from zad2testy import runtests
import random

def snow(S):
    n = len(S)
    if n == 0:
        return 0

    total_snow, day = 0, 0

    def calculate_total_snow(S, left, right):
        nonlocal total_snow, day

        if left == right and S[left] - day > 0:
            total_snow += S[left] - day
            day += 1
            return

        if left < right:
            q = parition(S, left, right)
            before = total_snow
            calculate_total_snow(S, q, right)
            if total_snow != before:
                calculate_total_snow(S, left, q-1)

    calculate_total_snow(S, 0, n-1)
    return total_snow


def parition(S, left, right):
    pivot_ind = random.randint(left, right)
    S[right], S[pivot_ind] = S[pivot_ind], S[right]

    pivot = S[right]
    i = left-1
    for j in range(left, right):
        if S[j] <= pivot:
            i += 1
            S[i], S[j] = S[j], S[i]
    S[i+1], S[right] = S[right], S[i+1]
    return i+1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)
