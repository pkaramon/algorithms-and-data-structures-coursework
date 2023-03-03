# 1 3 8 10 15 17 - sorted array
# we are given a number x
# find two indexes i, j such that:
# x = 9
# T[j]  - T[i] = 9 = x -> T[j] = 9 + T[i]
# 1 3 8 10 15 17 
# two "pointers" start at 0
# move them forward, depending on the difference

def find_ij(array, x):

    ...