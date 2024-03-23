# kmagiera@agh.edu.pl

"""
1. Zaimplementować quick sort żeby używał O(log n) pamięci.
Należy pamiętać o pamięci stosu.
2. InsertHeap
3. Zaimplementować QS bez rekurencji.
4. Napisać algorytm scalania k posortowanych list.
5. Zaproponować strukturę danych która pozwala na:
    - insert O(logn)
    - RemoveMax O(logn)
    - RemoveMin O(logn)
6. Zaproponować strukturę danych która pozwala na:
    - insert O(logn)
    - RemoveMedian O(logn)
7. Zaimplementować partition Hoare
"""


# InsertHeap
#                14
#     13                     12
#   5     7               3      4
# 15


def parent(i): return (i - 1) // 2


def left(i): return 2 * i + 1


def right(i): return 2 * i + 2


def heapify(heap, i, size):
    lt = left(i)
    rt = right(i)
    max_ind = i

    if lt < size and heap[lt] > heap[max_ind]:
        max_ind = lt
    if rt < size and heap[rt] > heap[max_ind]:
        max_ind = rt

    if max_ind != i:
        heap[max_ind], heap[i] = heap[i], heap[max_ind]
        heapify(heap, max_ind, size)


def heap_remove_max(heap, size):
    heap[size], heap[0] = heap[0], heap[size]
    heapify(heap, 0, size - 1)


def QS(T):
    n = len(T)
    stack = [(0, n - 1)]
    while len(stack) > 0:
        a, b = stack.pop()
        s = parition(T, a, b)
        if s - a > 1:
            stack.append((a, s))
        if b > s + 1:
            stack.append((s + 1, b))
    print(T)


def parition(T, lt, rt):
    x = T[rt]
    i = lt - 1
    for j in range(lt, rt):
        if T[j] <= x:
            i += 1
            T[j], T[i] = T[i], T[j]
    T[i + 1], T[rt] = T[rt], T[i + 1]
    return i + 1


def parition_hoare(S, left, right):
    """ 7.  """
    l = left
    r = right

    pivot = right
    while l < r:
        while S[l] < S[pivot] and l < r:
            l += 1
        while S[r] > S[pivot] and l < r:
            r -= 1
        S[l], S[r] = S[r], S[l]

    if S[l] > S[pivot]:
        middle = l
    else:
        middle = l + 1

    S[middle], S[pivot] = S[pivot], S[middle]
    return l


x = [5, 3, 2, 1, 5, 6, 2]
QS(x)
