def quick_select(A, left, right, k):
    while True:
        q = partition_quick_select(A, left, right)
        if q == k:
            return A[k]
        if k > q:
            left = q + 1
        else:
            right = q - 1


def partition_quick_select(A, left, right):
    pivot_ind = random.randint(left, right)
    A[pivot_ind], A[right] = A[right], A[pivot_ind]

    pivot = A[right]

    i = left - 1
    for j in range(left, right):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[right], A[i + 1] = A[i + 1], A[right]
    return i + 1
