import random


class Element:
    def __init__(self, value=None, max_i=-1, min_i=-1):
        self.max_i = max_i
        self.min_i = min_i
        self.value = value

    def __repr__(self) -> str:
        return f'({self.value}, {self.max_i}, {self.min_i})'


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return max(0, (i - 1) // 2)


class MaxMinQueue:
    def __init__(self):
        self.M = []
        self.m = []

    def insert(self, value):
        elem = Element(value, len(self.M), len(self.m))

        self.M.append(elem)
        i = len(self.M) - 1
        while (par := self.M[parent(i)]).val < self.M[i].val:
            par.max_i, elem.max_i = elem.max_i, par.max_i
            self.M[parent(i)], self.M[i] = self.M[i], self.M[parent(i)]
            i = parent(i)

        self.m.append(elem)
        i = len(self.m) - 1
        while (par := self.m[parent(i)]).val > self.m[i].val:
            par.min_i, elem.min_i = elem.min_i, par.min_i
            self.m[i], self.m[parent(i)] = self.m[parent(i)], self.m[i]
            i = parent(i)

    def delete_at(self, heap, i, cmp):
        root = self[0]
        heap[0], heap[i] = heap[i], heap[0]
        heap[-1], heap[0] = heap[0], heap[-1]

        pass

    def delete_root(self, heap, cmp):
        n = len(heap)
        if n == 0:
            raise LookupError('queue is empty')
        heap[-1], heap[0] = heap[0], heap[-1]
        value = heap.pop()

        heapify(heap, 0, n - 1, cmp)
        return value


queue = MaxMinQueue()
nums = list(range(100))
random.shuffle(nums)
for n in nums:
    queue.insert(n)
print(queue.M)
print(queue.m)


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


def heapify(heap, i, n, cmp: lambda child, ind: child < ind):
    ind = i
    lt, rt = left(i), right(i)

    if lt < n and cmp(heap[lt], heap[ind]):
        ind = lt
    if rt < n and cmp(heap[rt] > heap[ind]):
        ind = rt
    if ind != i:
        heap[ind], heap[i] = heap[i], heap[ind]
        heapify(heap, ind, n)


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
