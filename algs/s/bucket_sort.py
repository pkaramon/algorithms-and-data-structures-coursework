def bucket_sort(array, low, high):
    n = len(array)
    buckets = [[] for _ in range(n)]
    radius = (high-low) / n
    for x in array:
        buckets[int((x-low) / radius)].append(x)

    for buc in buckets:
        insertion_sort(buc)

    result = [None]*n
    i = 0

    for buc in buckets:
        for x in buc:
            result[i] = x
            i += 1
    return result


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        j = i
        value = array[i]
        while j >= 1 and array[j-1] > value:
            array[j] = array[j-1]
            array[j-1] = value
            j -= 1
