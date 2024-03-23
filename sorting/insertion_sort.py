def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        value = array[i]
        j = i - 1
        while j >= 0 and array[j] > value:
            array[j + 1] = array[j]
            array[j] = value
            j -= 1


def insertion_sort_2(array):
    for i in range(1, len(array)):
        j = i - 1
        while j >= 0 and array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1
