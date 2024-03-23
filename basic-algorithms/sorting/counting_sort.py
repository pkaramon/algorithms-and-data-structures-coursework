def counting_sort_unstable(arr):
    counters = [0 for _ in range(255)]
    for n in arr:
        counters[n] += 1

    i = 0
    for n, count in enumerate(counters):
        for _ in range(count):
            arr[i] = n
            i += 1


def counting_sort_stable(arr, k):
    n = len(arr)
    counts = [0] * k

    for x in arr:
        counts[x] += 1
    for i in range(1, k):
        counts[i] += counts[i - 1]

    output = [0] * n
    for i in range(n - 1, -1, -1):
        output[counts[arr[i]] - 1] = arr[i]
        counts[arr[i]] -= 1

    return output

# print(counting_sort_stable([7,9,8,6,2,1,3,9,9,2,3,6], 10))
