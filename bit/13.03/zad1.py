import math 

def sort_circle_points(points, k):
    n = len(points)
    if n == 0: return points
    buckets = [[] for _ in range(n)]

    radii = [0]*n
    radii[0] = k/math.sqrt(n)
    for i in range(1, n):
        radii[i] = math.sqrt(k**2/n + radii[i-1]**2)
    print(radii)
    

    


# key = 5
# 1 4 5 |6 7 12 3 3  132 1
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i
        while j>0 and arr[j-1] > arr[j]:
            arr[j] = arr[j-1]
            arr[j-1] = key
            j-=1


sort_circle_points([(1,2), (2,2), (-2, 0.5),(-4,0.75) ], 5)
