""" Piotr Karamon



"""

from zad2testy import runtests

def snow( S ):
    n = len(S)
    if n == 0:
        return 0

    total_snow, day = 0, 0
    def solve_v3(A, p, r):
        nonlocal total_snow
        nonlocal day
        if p == r and A[p] - day > 0:
            total_snow += A[p] - day
            day += 1
            return

        if p < r:
            q = parition(A, p, r)
            before = total_snow
            solve_v3(A,q, r)
            if total_snow != before:
                solve_v3(A,p, q-1)


    # def solve_v2(A):
    #     total_snow = 0
    #     day = 0
    #     stack= [(0, n-1)]
    #     while len(stack) != 0:
    #         p, r = stack.pop() 
    #         if p==r:
    #             2
    #             if A[p] - day > 0:
    #                 total_snow += A[p] - day
    #                 day += 1
    #                 continue
    #             else:
    #                 break
    #         q = parition(A, p, r)
    #         if q <= r:
    #             stack.append((q, r))
    #         if p <= q-1:
    #             stack.append((p, q-1))
    #     return total_snow

        

    solve_v3(S, 0, n-1)
    return total_snow


def solve_v2(A,total_snow=0):
    n = len(A)
    max_stack= [(0, n-1)]
    min_stack = []

    while len(max_stack) != 0:
        p, r = max_stack.pop() 
        q = parition(A, p, r)
        if q+1 <= r:
            max_stack.append((q+1, r))
        if p <= q:
            min_stack.append((p, q))
    
    day = 0
    total_snow =0
    while len(min_stack) != 0:
        p,r = min_stack.pop()
        quick_sort(A, p, r)
        for i in range(r, p-1, -1):
            if A[i] <= day:
                return total_snow
            total_snow += A[i] - day
            day += 1
    return total_snow


def solve(A):
    n = len(A)
    max_stack= [(0, n-1)]
    min_stack = []

    while len(max_stack) != 0:
        p, r = max_stack.pop() 
        q = parition(A, p, r)
        if q+1 <= r:
            max_stack.append((q+1, r))
        if p <= q:
            min_stack.append((p, q))
    
    day = 0
    total_snow =0
    while len(min_stack) != 0:
        p,r = min_stack.pop()
        quick_sort(A, p, r)
        for i in range(r, p-1, -1):
            if A[i] <= day:
                return total_snow
            total_snow += A[i] - day
            day += 1
    return total_snow



def quick_sort(A, p, r):
    while p < r:
        q = parition(A, p, r)
        quick_sort(A, p, q-1)
        p = q+1


def parition(A, p, r):
    pivot = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
