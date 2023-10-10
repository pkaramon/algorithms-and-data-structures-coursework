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
