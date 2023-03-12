def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = key


def insertion_sort_2(array):
    for i in range(1, len(array)):
        j = i-1
        while j >= 0 and array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            j -= 1