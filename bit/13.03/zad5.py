OUTLIERS_LENGTH = 10


def sort_numbers(nums, k):
    n = len(nums)
    outliers, n_outliers = [0] * OUTLIERS_LENGTH, 0

    counts = [0] * (k + 1)
    for x in nums:
        if 0 <= x and x <= k:
            counts[x] += 1
        else:
            outliers[n_outliers] = x
            n_outliers += 1

    insertion_sort(outliers, n_outliers)

    i, j = 0, 0
    while j < n_outliers and outliers[j] < 0:
        nums[i] = outliers[j]
        i, j = i + 1, j + 1

    for value, count in enumerate(counts):
        for _ in range(count):
            nums[i] = value
            i += 1

    for k in range(j, n_outliers):
        nums[i] = outliers[k]
        i += 1


# -1 -1 0 1 3 3 3 | 6 6 3
def insertion_sort(nums, size):
    for i in range(1, size):
        j = i - 1
        key = nums[i]
        while j >= 0 and nums[j] > nums[j + 1]:
            nums[j + 1] = nums[j]
            j -= 1
            nums[j + 1] = key


x = [1000, 0, 3, 2, -100, 7, 9, 3, 2, 3, 7, 32, 18, 5, -2]
sort_numbers(x, 9)
print(x)
