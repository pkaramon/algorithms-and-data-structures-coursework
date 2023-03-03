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


def binary_search2(array, n):
    p, k = 0, len(array) - 1
    while p <= k:
        m = (p+k) // 2
        if array[m] > n:
            k = m-1
        else:
            p = m+1
    if p <= len(array) -1 and array[p] == n:
        return p
    return -1