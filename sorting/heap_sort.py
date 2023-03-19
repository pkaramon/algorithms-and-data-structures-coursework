#         3,0
#     7,1     5,2
# 10,3 11,4 11,5 12,6
# 13,7          
# right(i) -> 


def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parrent(i): return (i-1) // 2

def heapify(A, i, n):
    lt, max_ind, rt = left(i), i, right(i)
    if lt < n and A[lt] > A[max_ind]:
        max_ind = lt 
    if rt < n and A[rt] > A[max_ind]:
        max_ind = rt 

    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A,max_ind,n)


def build_heap(A):
    n = len(A)
    for i in range(parrent(n-1), -1, -1):
        heapify(A, i, n)


def heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, 0, i)