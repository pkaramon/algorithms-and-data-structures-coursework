def partition(A, left, right):
    pivot = A[right]
    i = left - 1
    for j in range(left, right):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[right] = A[right], A[i+1]
    return i+1


def quick_sort(A, left, right):
    while left < right:
        q = partition(A, left, right)
        quick_sort(A, left, q-1)
        quick_sort(A, q+1, right)
