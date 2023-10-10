""" Piotr Karamon
Tworzę funkcje dynamiczną f(i,b) = minimalny koszt dotarcia do i-tej planety i posiadania b paliwa.

Jeżeli b = 0
To rozważamy wartości (j, 0) takie, że j< i oraz T[j][1] = i
i sprawdzamy czy dają nam minimalny koszt.


Również roważamy wariacje tankowań.
Jeżeli jesteśmy na i-tej planecie
to mogliśmy się do niej dostać z planety j bez użycia teleportu o ile D[i] - D[j] <= E
czyli o ile pozwala nam bak.
Następnie rozważam wariacje tankowań, czyli np.
    jeżeli przylecieliśmy ze stanu (j, D[i]-D[j]) to w i planecie musi dotankować b paliwa na planecie i.
    jeżeli przylecieliśmy ze stanu (j, D[i]-D[j] + 1) to w i planecie musi dotankować b-1 paliwa na planecie i.
    itd.


Czas: O(N*E*N*E) -> wielomianowa
Pamięć: O(N*E)

"""

from egz1btesty import runtests
from math import inf


def planets(D, C, T, E):
    n = len(D)
    f = [
        [inf for _ in range(E + 1)]
        for _ in range(n)
    ]

    f[0][0] = 0
    for e in range(E + 1):
        f[0][e] = C[0] * e

    def rec(i, b):
        if not (0 <= i < n and 0 <= b <= E):
            return inf

        if f[i][b] != inf:
            return f[i][b]

        if b == 0:
            for j in range(0, i):
                if T[j][0] == 0:
                    f[i][b] = min(f[i][b], rec(j, 0) + T[j][1])

        for j in range(0, i):
            if D[i] - D[j] <= E:
                for previous_fuel_level in range(D[i] - D[j], max(b + D[i] - D[j] + 1, E)):
                    f[i][b] = min(f[i][b],
                                  rec(j, previous_fuel_level) + (b-previous_fuel_level + (D[i] - D[j])) * C[i]
                                  )

        return f[i][b]

    print(f)

    return min(rec(n - 1, b) for b in range(0, E + 1))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=False)
