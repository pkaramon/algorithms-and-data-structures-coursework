def partition(A, left, right):
    mid = (left + right) // 2
    pivot = A[mid]
    i, j = left, right
    while i <= j:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    return mid


def quick_sort(A):
    if len(A) == 0:
        return
    stack = [(0, len(A) - 1)]
    while len(stack) > 0:
        left, right = stack.pop()
        if left < right:
            q = partition(A, left, right)
            stack.append((left, q - 1))
            stack.append((q + 1, right))
