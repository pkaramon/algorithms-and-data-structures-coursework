n = 4
k = 2
subset = [i for i in range(k)]

for _ in range(100):
    print(subset)
    if subset[k - 1] < n:
        j = k - 1
    else:
        j = k - 2
        while j >= 0 and subset[j] + 1 == subset[j + 1]:
            j -= 1

    if j >= 0:
        subset[j] += 1
        for i in range(j + 1, k):
            subset[i] = subset[i - 1] + 1
