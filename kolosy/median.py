import pprint


def select(matrix, k, left, right):
    q = partition(matrix, left, right)
    if q == k:
        return q
    if q < k:
        return select(matrix, k, q+1, right)
    else:
        return select(matrix, k, left, q-1)


def partition(matrix, left, right):
    N = len(matrix[0])
    pivot = matrix[right//N][right % N]
    i = left - 1
    for j in range(left, right):
        if matrix[j//N][j % N] < pivot:
            i += 1
            matrix[j//N][j % N], matrix[i//N][i % N] = matrix[i//N][i % N], matrix[j//N][j % N]

    matrix[(i+1)//N][(i+1) % N], matrix[right//N][right % N] =\
        matrix[right//N][right % N], matrix[(i+1)//N][(i+1) % N]

    return i+1


def median(matrix):
    if len(matrix) == 0 or len(matrix[0]) <= 1:
        return
    N = len(matrix[0])
    m = select(matrix, (N*(N-1)) // 2, 0, N*N-1)
    M = select(matrix, (N*(N+1))//2-1, 0, N*N-1)

    matrix[m//N][m % N], matrix[0][0] = matrix[0][0], matrix[m//N][m % N]
    matrix[M//N][M % N], matrix[1][1] = matrix[1][1], matrix[M//N][M % N]

    complete_diagonal(matrix, N, matrix[0][0], matrix[1][1])

    i = [1, 0]
    j = [N-2, N-1]

    while in_bounds(i, N) and in_bounds(j, N):
        while matrix[i[0]][i[1]] < m:
            i = i_inc(i, N)
        while matrix[j[0]][j[1]] > M:
            j = j_inc(j, N)
        matrix[i[0]][i[1]], matrix[j[0]][j[1]] = matrix[j[0]][j[1]], matrix[i[0]][i[1]]
        i = i_inc(i, N)
        j = j_inc(j, N)

    return matrix


def i_inc(i, N):
    i[1] += 1
    if i[0] == i[1]:
        i = [i[0]+1, 0]
    return i


def j_inc(j, N):
    j[1] -= 1
    if j[0] == j[1]:
        j = [j[0]-1, N-1]
    return j


def in_bounds(i, N):
    return -1 < i[0] < N and -1 < i[1] < N


def inc(i):
    i[1] += 1
    if i[0] == i[1]:
        i = [i[0]+1, 0]
    return i


def complete_diagonal(matrix, N, m, M):
    r = N-2
    for i in range(N):
        for j in range(N):
            if m < matrix[i][j] < M:
                matrix[N-r][N-r], matrix[i][j] = matrix[i][j], matrix[N - r][N-r]
                r -= 1
                if r == 0:
                    return


print(
    median([
        list(range(15, 20)),
        list(range(20, 25)),
        list(range(5, 10)),
        list(range(0, 5)),
        list(range(10, 15)),
    ]))
