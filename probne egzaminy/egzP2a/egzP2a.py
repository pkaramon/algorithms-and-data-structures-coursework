import random

from egzP2atesty import runtests

#
# for row:
#   
# 





def quick_sort(T, left, right):
    while left < right:
        q = parition(T, left, right)
        quick_sort(T, left, q-1)
        left = q+1


def parition(T, left, right):
    pivot_ind = random.randint(left, right)
    T[right], T[pivot_ind] = T[pivot_ind], T[right]

    pivot = T[right][1]
    i = left - 1
    for j in range(left, right):
        if T[j][1] > pivot:
            i += 1
            T[j], T[i] = T[i], T[j]
    T[i+1], T[right] = T[right], T[i+1]
    return i+1


def indexes(m, k):

    for row in range(m-1, -1, -1):
        print("ROW", row, ' -- ',  end='')
        prev = -m + (m-1) - row
        for i in range(0, k+row):
            i = prev + m - max(0, i-k)
            print(i, ' ',  end='')

            prev = i
        print()

    last_in_row = -1
    for row in range(m-1, -1, -1):
        prev = -m + (m-1) - row
        # row_highest = magic_fives(T, 0, n-1, )
        indexes = []
        for i in range(0, k+row):
            i = prev + m - max(0, i-k)
            indexes.append(i)
            prev = i
        last_in_row += k+row
        print('last in row', last_in_row)


indexes(4, 3)



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
        while j - 1 >= left and A[j-1][1] < key[1]:
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


def zdjecie(T, m, k):
    n = len(T)

    taken = [False]*n
    last_in_row = -1

    copy = [T[i] for i in range(n)]

    for row in range(m-1, -1, -1):
        prev = -m + (m-1) - row
        last_in_row += k+row
        row_least_high = magic_fives(copy, 0, n-1, last_in_row)

        index = 0

        for i in range(0, k+row):
            i = prev + m - max(0, i-k)

            while index < n:
                if T[index][1] >= row_least_high[1] and not taken[index]:
                    taken[index] = True
                    T[index], T[i] = T[i], T[index]
                    break
                index+=1

            prev = i
        
    # quick_sort(T, 0, n-1)
    # temp = [T[i] for i in range(n)]
    # temp_i = 0

    # for row in range(m-1, -1, -1):
    #     prev = -m + (m-1) - row
    #     indexes = []
    #     for i in range(0, k+row):
    #         i = prev + m - max(0, i-k)

    #         T[i] = temp[temp_i]
    #         temp_i += 1

    #         prev = i

    # return None
runtests(zdjecie, all_tests=False)