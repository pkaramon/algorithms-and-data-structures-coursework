import random


def partition(array, left, right):
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


def select(array, k, left, right):
    while True:
        q = partition(array, left, right)
        if q == k:
            return q
        elif q < k:
            left = q + 1
        else:
            right = q - 1


nums = list(range(100))
random.shuffle(nums)
print(nums)
print([select(nums, k, 0, len(nums) - 1) for k in range(100)])
