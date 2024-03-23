from random import randint


def soldiers(array, p, q):
    H = select(array, p)
    h = select(array, q)

    result = [0] * (q - p + 1)
    result[0] = H
    result[-1] = h
    i = 1

    for height in array:
        if h < height < H:
            result[i] = height
            i += 1

    quick_sort(result, 0, (q - p))
    return result


def quick_sort(array, left, right):
    if left < right:
        q = partition(array, left, right)
        quick_sort(array, left, q - 1)
        quick_sort(array, q + 1, right)


def partition(array, left, right):
    pivot_ind = randint(left, right)
    array[right], array[pivot_ind] = array[pivot_ind], array[right]

    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] > pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


def select(array, k):
    left, right = 0, len(array) - 1
    while True:
        q = partition(array, left, right)
        if k == q:
            return array[q]
        if k > q:
            left = q + 1
        else:
            right = q - 1


print(soldiers([0, 2, 3, 1, 9, 5, 6, 7, 8, 4], 3, 8))
