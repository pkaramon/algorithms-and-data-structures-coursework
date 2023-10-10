from math import inf


def k_sum(numbers, k):
    n = len(numbers)
    dist = [inf] * n

    for i in range(k):
        dist[i] = 0

    for i in range(n):
        for j in range(min(i + k + 1, n)):
            if dist[i] + numbers[i] < dist[j]:
                dist[j] = dist[i] + numbers[i]
    print(dist)

    answer = inf
    for j in range(n-k, n):
        answer = min(answer, dist[j] + numbers[j])
    return answer


print(k_sum([1,2,5,4, 6, 15, 8, 100, 12, 13, 15, 21], 4))
print(k_sum([1,2,5,4, 6, 15, 8, 7], 4))
