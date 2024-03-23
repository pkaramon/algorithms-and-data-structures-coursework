from collections import deque
from math import inf

from zad8testy import runtests


def plan(T):
    m = len(T[0])

    oil = get_oil_spils(T)

    f = [inf for _ in range(m)]
    g = [0 for _ in range(m)]

    g[0] = oil[0]
    f[0] = 0

    for i in range(1, m):
        for j in range(i):
            if g[j] - (i - j) >= 0 and f[j] + 1 < f[i]:
                f[i] = f[j] + 1
        for j in range(i):
            if f[i] == f[j] + 1 and g[j] - (i - j) + oil[i] > g[i]:
                g[i] = g[j] - (i - j) + oil[i]
    print(oil)
    print(f, g)
    return f[m - 1]


NEIGHBOURS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def neighbours(n, m, a, b):
    for (a_offset, b_offset) in NEIGHBOURS:
        x, y = a + a_offset, b + b_offset
        if 0 <= x < m and 0 <= y < n:
            yield x, y


def get_oil_spils(T):
    n = len(T)
    m = len(T[0])

    visited = [[False for _ in range(m)] for _ in range(n)]

    return [calculate_oil_for(i, T, visited) for i in range(m)]


def calculate_oil_for(i, T, visited):
    if visited[0][i] or T[0][i] == 0:
        return 0

    n, m = len(T), len(T[0])
    q = deque()
    q.append((0, i))
    oil = T[0][i]
    visited[0][i] = True

    while len(q) > 0:
        a, b = q.popleft()
        for (x, y) in neighbours(n, m, a, b):
            if not visited[x][y] and T[x][y] > 0:
                q.append((x, y))
                visited[x][y] = True
                oil += T[x][y]
    return oil


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
