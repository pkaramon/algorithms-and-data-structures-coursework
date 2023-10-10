def nds(k, numbers):
    n = len(numbers)
    rems = [0 for _ in range(k)]

    for x in numbers:
        rems[x % k] += 1

    for r in range(k):
        if (2 * r) % k == 0:
            rems[r] = min(1, rems[r])

    F = [0 for _ in range(k)]
    F[0] = rems[0]

    for i in range(1, k):
        if (k - i) % k >= i:
            F[i] = F[i - 1] + rems[i]
        else:
            F[i] = max(F[i - 1], F[i - 1] + rems[i] - rems[(k - i) % k])
    return F[n - 1]


print(nds(4, [19, 10, 12, 10, 24, 25, 22]))
