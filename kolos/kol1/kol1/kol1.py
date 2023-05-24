""" Piotr Karamon
Algorytm przechodzi przez każdy przedział, tworzy kopię tego przedziału a
następnie używa algorytmu magicznych piątek by znaleźć k-ty największy
element w tym przedziale i dodaje go do sumy.

Zewnętrzna pętla wykonuje się co najwyżej n razy:
    wewnętrz niej tworzymy kopię p-elementową czyli p
    oraz szukamy k-tej co do wielkości liczby w tej tablicy czyli również p 
Zatem złożoność czasowa to n*(2p)

Czas: O(np)
Pamięć: O(p)
"""

from kol1testy import runtests

def ksum(T, k, p):
    n = len(T)
    total = 0
    for i in range(n-p+1):
        copy = T[i:i+p]
        total += magic_fives(copy, 0,p-1, p-k)
    return total


def magic_fives(A, left, right, k):
    size = right - left + 1
    if size <= 5:
        insertion_sort(A, left, right)
        return A[k]

    medians = []
    for i in range(size//5):
        medians.append(get_median(A, left + i*5, left + i*5 + 4))
    if size % 5 > 0:
        medians.append(get_median(A, left+len(medians)*5, right))
    median = magic_fives(medians, 0, len(medians)-1, len(medians)//2)
    q = partition(A, left, right, median)
    if q == k:
        return A[k]
    elif k > q:
        return magic_fives(A, q+1, right, k)
    else:
        return magic_fives(A, left, q-1, k)


def get_median(A, left, right):
    n = right-left + 1
    temp = A[left:left+n]
    insertion_sort(temp, 0, n-1)
    return temp[n//2]


def insertion_sort(A, left, right):
    i = left+1
    for j in range(i, right+1):
        value = A[j]
        while j - 1 >= left and A[j-1] > value:
            A[j] = A[j-1]
            A[j-1] = value
            j -= 1


def partition(A, left, right, pivot):
    for i in range(left, right+1):
        if A[i] == pivot:
            A[right], A[i] = A[i], A[right]
            break

    i = left-1
    for j in range(left, right):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[right], A[i+1] = A[i+1], A[right]
    return i+1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )


