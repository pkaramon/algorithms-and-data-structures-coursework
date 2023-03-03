def quick_sort(arr, left, right):
    middle = (left+right) // 2 
    pivot = arr[middle]
    i,j = left, right
    while i<=j:
        while arr[i] > pivot:
            arr[i], arr[j] = arr[j], arr[j]
            j+=1
        



