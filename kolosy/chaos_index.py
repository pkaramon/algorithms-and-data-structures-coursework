def chaos_index(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], i)
    merge_sort(T, 0, n-1, lambda x,y: x[0]<=y[0])
    print(T)
    return max(abs(T[i][1]-i) for i in range(n))

    

def merge_sort(T, left, right,  cmp):
    if left == right:
        return
    mid = (left+right) // 2
    merge_sort(T, left, mid, cmp) # [left, mid]
    merge_sort(T, mid+1, right, cmp) # (mid, right]
    merge(T, left, mid, right, cmp)

# T1: [left, mid] 
# T2: (mid, right]
def merge(T, left, mid, right, cmp):
    temp = [0]*(right-left+1)
    k = 0

    i, j = left, mid+1
    while i <= mid and j <= right:
        if cmp(T[i], T[j]):
            temp[k] = T[i]
            i+=1
        else:
            temp[k] = T[j]
            j += 1
        k+=1
    
    while i <= mid:
        temp[k] = T[i]
        k += 1
        i += 1

    while j <= right:
        temp[k] = T[j]
        k+= 1
        j += 1
    
    for i in range(left, right+1):
        T[i] = temp[i - left]




    
# import random
# ns = list(range(100))
# random.shuffle(ns)
# merge_sort(ns, 0, len(ns)-1)
# print(ns)
    
def cmp(x, y):
    print(x, y)
    return x[1] <= y[1]

points = [ (0, 3),(2,2) ,(4, 3)]
merge_sort(points, 0, len(points)-1, cmp)
print(points)

print(chaos_index([0, 2, 1.1, 2]))