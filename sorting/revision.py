# bubble sort
def bubble_sort(array):
    n = len(array)
    for i in range(0, n):
        for j in range(1, n-i):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]

# selection sort


def selection_sort(array):
    n = len(array)
    for i in range(0, n):
        k = i
        for j in range(i+1, n):
            if array[j] < array[k]:
                k = j
        array[i], array[k] = array[k], array[i]

# insertion sort


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        value = array[i]
        j = i-1
        while j >= 0 and array[j] > value:
            array[j+1] = array[j]
            array[j] = value
            j -= 1

# counting sort


def counting_sort_inplace(array):
    counts = [0] * 1000
    for x in array:
        counts[x] += 1

    i = 0
    for v in range(len(counts)):
        for _ in range(counts[v]):
            array[i] = v
            i += 1


def counting_sort(array, n_counts=1000):
    counts = [0] * n_counts
    for x in array:
        counts[x] += 1

    for i in range(1, n_counts):
        counts[i] += counts[i-1]

    output = [0]*len(array)
    for i in range(len(array)-1, -1, -1):
        output[counts[array[i]]-1] = array[i]
        counts[array[i]] -= 1

    for i in range(len(array)):
        array[i] = output[i]

# merge sort


def merge_sort_tests(A):
    if len(A) == 0:
        return
    merge_sort(A, 0, len(A)-1)


def merge_sort(A, start, end):
    if start >= end:
        return
    middle = (start+end) // 2
    merge_sort(A, start, middle)
    merge_sort(A, middle+1, end)
    merge(A, start, middle, end)


def merge(A, start, middle, end):
    aux_space = [0] * (end-start+1)
    k = 0

    i, j = start, middle+1
    while i <= middle and j <= end:
        if A[i] < A[j]:
            aux_space[k] = A[i]
            i += 1
        else:
            aux_space[k] = A[j]
            j += 1
        k += 1
    for x in range(i, middle+1):
        aux_space[k] = A[x]
        k += 1
    for x in range(j, end+1):
        aux_space[k] = A[x]
        k += 1

    for i in range(start, end+1):
        A[i] = aux_space[i-start]

# heap sort


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


def partition(array, left, right):
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[right] = array[right], array[i+1]
    return i+1


def part(A, left, right):
    mid = (left+right) // 2
    pivot = A[mid]
    i, j = left, right
    while i <= j:
        while A[i] < pivot: i += 1
        while A[j] > pivot: j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    
    return mid


def quick_sort(A):
    qs(A, 0, len(A)-1)

def qs(A, left, right):
    if left < right:
        q = part(A, left, right)
        qs(A, left, q-1)
        qs(A, q+1, right)


x = [2, 4, 3, 7, 7, 7, 2, 8, 3, 5, 9]
# x = [7,7,7,7,7]

quick_sort(x)
print(x)
