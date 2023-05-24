# sorted array
# find i and j such that T[i] + T[j] = x
# in O(n)

# we set i = 0 and j = n-1
# if T[i] + T[j] > x -> j -= 1
# if T[i] + T[j] < x -> i +=1
# else: we found it

def findij(T, x):
    n = len(T)
    i, j = 0, n-1
    while i != j:
        if T[i] + T[j] == x:
            return i, j
        elif T[i] + T[j] > x:
            j -= 1
        else:
            i += 1
    return -1, -1
    
print(findij([2, 3, 5, 7, 10, 15, 28], 32))
