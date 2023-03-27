import random
N_COUNTS = 20


def pretty_sort(nums):
    n = len(nums)

    nw = [0]*n
    for i in range(n):
        _, w = calcjw(nums[i])
        nw[i] = w

    counts = [0] * N_COUNTS
    for i in range(n):
        counts[nw[i]] += 1

    for i in range(1, N_COUNTS):
        counts[i] += counts[i-1]

    sorted_by_w = [0]*n
    for i in range(n-1, -1, -1):
        sorted_by_w[counts[nw[i]] - 1] = nums[i]
        counts[nw[i]] -= 1

    print('by w', sorted_by_w)

    nj = [0]*n
    for i in range(n):
        j, _ = calcjw(sorted_by_w[i])
        nj[i] = j

    counts = [0] * N_COUNTS
    for i in range(n):
        counts[nj[i]] += 1

    for i in range(n-2, -1, -1):
        counts[i] += counts[i+1]

    print(counts)
    output = [0]*n
    for i in range(n-1, -1, -1):
        output[counts[nj[i]] - 1] = sorted_by_w[i]
        counts[nj[i]] -= 1
    print(output)


def rev_counting_sort(array, k):
    n = len(array)
    counts = [0] * k
    for i in range(n):
        counts[array[i]] += 1

    for i in range(k-2, -1, -1):
        counts[i] += counts[i+1]

    output = [0]*n
    for i in range(n):
        output[counts[array[i]] - 1] = array[i]
        counts[array[i]] -= 1
    return output


def calcjw(n):
    digits = [0]*9
    while n > 0:
        digits[n % 10] += 1
        n //= 10

    j, w = 0, 0
    for d in digits:
        if d == 1:
            j += 1
        if d > 1:
            w += 1
    return j, w


pretty_sort([455, 123, 114577, 67333, 1266, 333, 2344,  22,
            1, 8, 33,  2, 4444, 223344,  38,])
