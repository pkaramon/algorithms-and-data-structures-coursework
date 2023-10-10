def quick_sort(arr):
    quick_sort_internal(arr, 0, len(arr) - 1)


def quick_sort_internal(A, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    pivot = A[mid]
    i, j = left, right

    while i < j:
        while A[i] < pivot: i += 1
        while A[j] > pivot: j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

    if left < j: quick_sort_internal(A, left, j)
    if i < right: quick_sort_internal(A, i, right)


a = [4, 7, 8, 1, 3, 5, 8, 2, 1]
quick_sort(a)
print(a)
