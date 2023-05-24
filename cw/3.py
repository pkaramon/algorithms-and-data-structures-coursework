# poprzednie ćwiczenia

# 0
# RemoveMax
# RemoveMin
# Insert
# wszystko w logn
#
# robimy dwa kopce MAX i MIN
# insert -> insert into both
#
# for each element we need to know:
#   max_i, min_i, value
#
# how to remove an element from middle of a heap:
#   do removeMax and insert kinda
# we take last element and swap it with one with we wan tot
#

# 1
# insert() O(logn)
# RemoveMedian() O(logn) we only remove when n is odd
# two heaps MAX and MIN
#    MAX          MIN
#     (n-1)/2    (n-1)/2
# |          ||           |
#  median is the root of MAX heap
#
# root MAX = 15, root MIN = 20
#
# insert(25) ->
# 25 > root MIN -> insert into MIN
# now median -> (max root + min root) / 2
#
# insert(30) -> insert into MIN
# throw 1 element from MIN heap to MAX heap
#
# insert(10) -> insert into MAX
#       throw 1 element from MAX heap to MIN heap
#

import numpy


def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return max(0, (i-1)//2)


def insert_maxheap(heap, element):
    heap.append(element)
    i = len(heap)-1
    while heap[parent(i)] < heap[i]:
        heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
        i = parent(i)


def insert_minheap(heap, element):
    heap.append(element)
    i = len(heap)-1
    while heap[parent(i)] > heap[i]:
        heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
        i = parent(i)


def heapify_max(heap, i, n):
    max_ind = i
    lt, rt = left(i), right(i)

    if lt < n and heap[lt] > heap[max_ind]:
        max_ind = lt
    if rt < n and heap[rt] > heap[max_ind]:
        max_ind = rt

    if max_ind != i:
        heap[max_ind], heap[i] = heap[i], heap[max_ind]
        heapify_max(heap, max_ind, n)


def heapify_min(heap, i, n):
    min_ind = i
    lt, rt = left(i), right(i)

    if lt < n and heap[lt] < heap[min_ind]:
        min_ind = lt
    if rt < n and heap[rt] < heap[min_ind]:
        min_ind = rt

    if min_ind != i:
        heap[min_ind], heap[i] = heap[i], heap[min_ind]
        heapify_max(heap, min_ind, n)



class MedianQueue:
    def __init__(self) -> None:
        self.M = []
        self.m = []

    def insert(self, value):
        if len(self.M) == len(self.m):
            insert_maxheap(self.M, value)
        else:
            insert_minheap(self.m, value)
    
    def remove_median(self):
        self.M[-1], self.M[0] = self.M[0], self.M[-1]
        median = self.M.pop()
        heapify_max(self.M, 0, len(self.M))

        if len(self.M) < len(self.m):
            self.m[-1], self.m[0] = self.m[0], self.m[-1]
            x = self.m.pop()
            heapify_min(self.m)
            insert_maxheap(self.M, x)
        return median

q = MedianQueue()
nums = [1,2,3,4,5,6,7]
import random
random.shuffle(nums)
for n in nums:
    q.insert(n)
print(q.M, q.m)
print(q.remove_median())

# 2
# Algorytm znajdowania k-tego co do wielkości elementu
# w tablicy nieposortowanej
# pdobnie jak quick sort
# magiczne piątki -> zawsze O(n)
# partition theta(n) O(n^2)

# nowe zadania

# 3
# algorytm sortujący n-elementową tablicę liczb z zakresu 0,1,...,n^2
# w czasie liniowym
def sort_numbers(nums):
    n = len(nums)
    if n == 0:
        return nums
    nums = counting_sort(nums, lambda x: x % n, n)
    nums = counting_sort(nums, lambda x: x // n, n)
    return nums

#


def counting_sort(nums, get_digit, d):
    n = len(nums)
    counts = [0] * d

    for x in nums:
        counts[get_digit(x)] += 1

    for i in range(1, n):
        counts[i] += counts[i-1]

    output = [0] * n
    for i in range(n-1, -1, -1):
        d = get_digit(nums[i])
        output[counts[d]-1] = nums[i]
        counts[d] -= 1

    return output


# 4
# posortuj tablicę długości n, która posiada logn różnych elementów
# mapowanie (0, 1, ..., logn)
# binary search ->
#
#  O(n*log(logn) + logn * logn) = O(nlogn*logn)
#

# 5
# sprawdź czy słowa a i b są anagramami -
# czy b jest jakąś permutacją a
# a) a-z alfabet angielski
# b) dowolne symbol z tablicy Unicode
# a


def are_anagrams(a: str, b: str) -> bool:
    a_counts = [0] * 26
    b_counts = [0] * 26
    for char in a:
        a_counts[ord(char) - ord('a')] += 1
    for char in b:
        b_counts[ord(char) - ord('a')] += 1
    return a_counts == b_counts


# b

c = numpy.empty(2**21)


def are_anagrams_unicode(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    n = len(a)

    for i in range(n):
        c[ord(a[i])] = 0
        c[ord(b[i])] = 0

    for i in range(n):
        c[ord(a[i])] += 1
        c[ord(b[i])] -= 1

    for i in range(n):
        # if c[ord(a[i])] != 0 or c[ord(b[i])] != 0:
        if c[ord(a[i])] != 0:
            return False
    return True


# 6
# Tablica A zawiera n parami różnych liczb
# znaleźć liczby x i y z tablicy A,
# takie, że x - y jest największa i że nie istnieje
# liczba k która należy do A, że y < k < x
#
# 1 2 3 7 10
#  1 1 4 3


# 10-7 = 3
# 7 -3 =4
# basic O(logn) -> sort it and compare elements which are next to each other
# O(n) -> ?????
# sortowanie kubuełkowe
# min, max -> i dzielimy przediał na [min, max] na  n kubełków
# w każdym kubełku obchodzą nas min, max
# check max i min
# jeśli każdy kubełek zapełniony
#
