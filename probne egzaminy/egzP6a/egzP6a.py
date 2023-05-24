from egzP6atesty import runtests


def google(H, s):
    # max_length = len(max(H, key=len))
    n = len(H)
    aux = [(len(H[i]), letters(H[i]), i) for i in range(n)]
    x = magic_fives(aux, 0, n-1, n - s)
    return H[x[2]]


def counting_sort(H, key, k):
    n = len(H)

    counts = [0]*k
    for h in H:
        counts[h[key]] += 1

    for i in range(1, k):
        counts[i] += counts[i-1]

    output = [0]*n
    for i in range(n-1, -1, -1):
        output[counts[H[i][key]] - 1] = H[i]
        counts[H[i][key]] -= 1
    return output


def left(i): return 2*i+1
def right(i): return 2*i+2
def parent(i): return (i-1) // 2


def heapify(heap, i, n):
    max_ind = i
    lt, rt = left(i), right(i)

    if lt < n and heap[lt] > heap[max_ind]:
        max_ind = lt
    if rt < n and heap[rt] > heap[max_ind]:
        max_ind = rt

    if max_ind != i:
        heap[max_ind], heap[i] = heap[i], heap[max_ind]
        heapify(heap, max_ind, n)


def buildheap(array):
    n = len(array)
    for i in range(parent(n-1), -1, -1):
        heapify(array, i, n)


def heapsort(array):
    n = len(array)
    buildheap(array)
    for heap_end in range(n-1, 0, -1):
        array[0], array[heap_end] = array[heap_end], array[0]
        heapify(array, 0, heap_end)


def letters(string: str):
    count = 0
    for char in string:
        if char.isalpha():
            count += 1
    return count


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
        key = A[j]
        while j - 1 >= left and A[j-1] > key:
            A[j] = A[j-1]
            A[j-1] = key
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


runtests(google, all_tests=True)
