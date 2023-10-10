from zad1ktesty import runtests


def roznica(S):
    n = len(S)
    v = lambda i: 1 if S[i] == '0' else -1
    m = -1
    for col in range(n):
        value = 0
        for row in range(col, n):
            value += v(row)
            m = max(value, m)
    return m


runtests(roznica)
