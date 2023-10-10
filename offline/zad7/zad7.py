""" Piotr Karamon
Do dowolnego punktu (i, j) mogliśmy się dostać:
1) z punktu (i, j-1)
2) z punktu (i+1, j)
3) z punktu (i-1, j)
modulo corner case'y

Algorytm polega na obliczaniu dwóch funkcji. UP i DOWN skrótowo U i D

U(i,j) - długość najdłuższej ścieżki z (0,0) do (i, j) ale takiej
        że do (i, j) "doszliśmy idąc do góry"

D(i,j) - długość najdłuższej ścieżki z (0,0) do (i, j) ale takiej
        że do (i, j) "zeszliśmy od góry"

U(0, 0) = 0
D(0, 0) = 0

U(i, j) = max(U(i, j-1), D(i, j-1), U(i+1, j)) + 1
D(i, j) = max(U(i, j-1), D(i, j-1), D(i-1, j)) + 1

Jeśli (i, j) to przeszkoda to nie obliczam dla tej komórki tych funkcji. Czyli pozostają one równe -inf.

Po obliczeniu tych funkcji nasza odpowiedź to max(U(i, j), D(i, j))

Czas:   O(n^2)
Pamięć: O(n^2)
"""
from zad7testy import runtests


def maze(L):
    n = len(L)
    U = [[float('-inf')] * n for _ in range(n)]
    D = [[float('-inf')] * n for _ in range(n)]
    U[0][0] = 0
    D[0][0] = 0

    for row in range(1, n):
        if L[row][0] != '#':
            D[row][0] = D[row - 1][0] + 1

    for col in range(1, n):
        if L[0][col] != '#':
            D[0][col] = max(D[0][col - 1], U[0][col - 1]) + 1
        for row in range(1, n):
            if L[row][col] != '#':
                D[row][col] = max(D[row][col - 1], U[row][col - 1], D[row - 1][col]) + 1

        if L[n - 1][col] != '#':
            U[n - 1][col] = max(D[n - 1][col - 1], U[n - 1][col - 1]) + 1
        for row in range(n - 2, -1, -1):
            if L[row][col] != '#':
                U[row][col] = max(D[row][col - 1], U[row][col - 1], U[row + 1][col]) + 1

    result = max(U[n - 1][n - 1], D[n - 1][n - 1])
    return result if result != float('-inf') else -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)



