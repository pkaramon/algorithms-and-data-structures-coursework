def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i-1) // 2


def heapify(heap, i, n):
    max_ind = i
    lt, rt = left(i), right(i)
    if lt < n and heap[lt] > heap[max_ind]:
        max_ind = lt
    if rt < n and heap[rt] > heap[max_ind]:
        max_ind = rt

    if max_ind != i:
        heap[i], heap[max_ind] = heap[max_ind], heap[i]
        heapify(heap, max_ind, n)


def build_heap(array):
    n = len(array)
    for i in range(parent(n-1), -1, -1):
        heapify(array, i, n)


def heapsort(array):
    build_heap(array)
    n = len(array)
    for heap_end in range(n-1, 0, -1):
        array[0], array[heap_end] = array[heap_end], array[0]
        heapify(array, 0, heap_end)
