# given an array of natural numbers (len = n)
# range of values [0, n^2 -1]
# sort it in O(n)

# n = 3
# 9 - possible values
# 0,1,2  3,4,5, 6,7,8
# [0,0,0,]

def sort_numbers(nums):
    n = len(nums)
    if n == 0: return nums
    nums = counting_sort(nums, lambda x: x % n, n)
    nums = counting_sort(nums, lambda x: x // n, n)
    return nums

#  
def counting_sort(nums, get_digit, d):
    n = len(nums)
    counts = [0] *  d

    for x in nums:
        counts[get_digit(x)] += 1

    for i in range(1, n):
        counts[i] += counts[i-1]
    
    output = [0] * n
    for i in range(n-1, -1, -1):
        d = get_digit(nums[i])
        output[counts[d]-1] = nums[i]
        counts[d] -= 1

    return output


#  
print(sort_numbers([99, 25, 1, 43,0, 5, 77, 55, 9, 13,]))