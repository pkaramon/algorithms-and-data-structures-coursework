class PriorityQueue:
    def __init__(self, numbers) -> None:
        self.heap = numbers
        buildheap(self.heap)

    def peek_max(self):
        if self.n == 0:
            raise LookupError('queue is empty')

        return self.heap[0]

    def extract_max(self):
        if self.n == 0:
            raise LookupError('queue is empty')

        max = self.heap[0]
        self._swap(self.n - 1, 0)
        heapify(self.heap, 0, self.n - 1)
        self.heap.pop()
        return max

    def insert(self, x):
        self.heap.append(x)
        i = self.n - 1
        while self.heap[parent(i)] < self.heap[i]:
            self._swap(parent(i), i)
            i = parent(i)

    @property
    def n(self):
        return len(self.heap)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return max(0, (i - 1) // 2)


def heapify(heap, i, n):
    max_ind = i
    lt, rt = left(i), right(i)
    max_ind = lt if lt < n and heap[lt] > heap[max_ind] else max_ind
    max_ind = rt if rt < n and heap[rt] > heap[max_ind] else max_ind
    if max_ind != i:
        heap[max_ind], heap[i] = heap[i], heap[max_ind]
        heapify(heap, max_ind, n)


def buildheap(numbers):
    n = len(numbers)
    for i in range(parent(n - 1), -1, -1):
        heapify(numbers, i, n)


pq = PriorityQueue([1, 3, 10, 7, 4, 8])
buildheap(pq.heap)
print(pq.heap)
pq.insert(3)
pq.insert(8)
pq.insert(9)
pq.insert(5)
print(pq.extract_max())
print(pq.extract_max())
print(pq.extract_max())
print(pq.extract_max())
print(pq.extract_max())
print(pq.extract_max())
print(pq.extract_max())
