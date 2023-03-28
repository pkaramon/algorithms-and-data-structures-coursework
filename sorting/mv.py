def magic_fives(A, left, right, k):
    size = right - left + 1
    if size <= 5:
        insertion_sort(A, left, right)
        return A[k]

    medians = []
    for i in range(size//5):
        medians.append(get_median(A, left + i*5, left + i*5 + 4))
    if size % 5 > 0:
        medians.append(get_median(A, left+len(medians)*5, right))
    median = magic_fives(medians, 0, len(medians)-1, len(medians)//2)
    q = partition(A, left, right, median)
    if q == k:
        return A[k]
    elif k > q:
        return magic_fives(A, q+1, right, k)
    else:
        return magic_fives(A, left, q-1, k)


def get_median(A, left, right):
    n = right-left + 1
    temp = A[left:left+n]
    insertion_sort(temp, 0, n-1)
    return temp[n//2]


def insertion_sort(A, left, right):
    i = left+1
    for j in range(i, right+1):
        key = A[j]
        while j - 1 >= left and A[j-1] > key:
            A[j] = A[j-1]
            A[j-1] = key
            j -= 1

def partition(A, left, right, pivot):
    for i in range(left, right+1):
        if A[i] == pivot:
            A[right], A[i] = A[i], A[right]
            break

    i = left-1
    for j in range(left, right):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[right], A[i+1] = A[i+1], A[right]
    return i+1

