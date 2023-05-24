def binary_search(array, n):
    p, k = 0, len(array) - 1
    while p <= k:
        m = (p+k) // 2
        if array[m] == n:
            return m
        elif array[m] > n:
            k = m-1
        else:
            p = m+1
    return -1
