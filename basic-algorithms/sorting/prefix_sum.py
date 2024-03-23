def create_prefix_sum(numbers):
    n = len(numbers)
    prefix_sum = [0] * n
    prefix_sum[0] = numbers[0]

    for i in range(1, n):
        prefix_sum[i] += prefix_sum[i - 1] + numbers[i]
    return prefix_sum


def sum_from_i_to_j(prefix_sums, numbers, i, j):
    return prefix_sums[j] - prefix_sums[i] + numbers[i]
