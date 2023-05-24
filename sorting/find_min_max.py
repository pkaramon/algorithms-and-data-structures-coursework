# find min and max for array
# obvious soluion ~ 2n
# not obvious 3/2n
# 2 8 | 3 1 4 7 6 5 10 2
# m=2 M=8
# take next two (3 and 1) and compare
# then compare with m and M apropriately
import random

def minmax(array):
    min, max = array[0], array[0]
    for i in range(len(array) % 2, len(array), 2):
        x, y = array[i], array[i+1]
        if x > y:
            if x > max:
                max = x
            if y < min:
                min = y
        else:
            if y > max:
                max = y
            if x < min:
                min = x
    return min, max

            
x = list(range(100))
random.shuffle(x)
print(minmax(x))


    

