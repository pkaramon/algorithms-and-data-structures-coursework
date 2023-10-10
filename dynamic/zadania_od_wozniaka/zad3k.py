from zad3ktesty import runtests


def easy_extend(F, a, b, k):
    if b - a + 1 <= k:
        return True
    return  not all(F[a][x] == F[a][b - 1] for x in range(b - k + 1, b))



def ksuma(T, k):
    n = len(T)
    F = [[float('inf')] * n for _ in range(n)]

    m = float('inf')

    for a in range(n):
        F[a][a] = T[a]
        for b in range(a + 1, n):
            if easy_extend(F, a, b, k):
                F[a][b] = F[a][b-1]
            else:
                F[a][b] = min(F[a][x] + T[x] for x in range(b-k+1, b+1) )
            if b-a + 1 >= k:
                m = min(m, F[a][b])

    print(m, F)



    return 0


runtests(ksuma)
