def counting_sort(arr):
    counters = [0 for _ in range(255)]
    for n in arr:
        counters[n] += 1

    i = 0
    for n, count in enumerate(counters):
        for _ in range(count):
            arr[i] = n
            i += 1
