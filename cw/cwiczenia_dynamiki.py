"""
1. Wędrówka po szachownicy
Dana szachowanica nxn.
Są dwa pola specjalne (0,0) (n-1, n-1) -> start, koniec
Wędrówka z ze startu do końca.
Możliwe ruchy: w prawo alb w dół.
M[i][j] -> koszt przejścia przez dane pole
Znajdź najtańszą ścieżkę.


f(x,y) = min( f(x-1, y), f(x, y-1)) + A[x][y]
"""


def money(coins, amount):
    """
    2. Wydawanie monet.
    Dana tablica nominałów -> N = [1, 5, 8]
    Mamy liczbę t -> kwota którą chcemy wydać.
    Chcemy wydać t w najmniejszej liczbie monet.
    W normalnym kraju -> n(i+1) >= 2*n(i)
        -> zachłannie


    f(kwota t, i) -> ile najmniej monet potrzeba by wydać t korzystając z pierwszych i monet
    f(t, i) = min 0<=j<=i-1(f(t-A[i], j))



    """

    n = len(coins)


def subset_sum(A, T):
    """
    Suma podzbioru.
    Tablica liczb naturalnych A = [...]
    Mamy sumę T - suma

    Stwierdzić czy można znaleźć podzbiór A tak żeby zsumował się do sumy T.

    Tablica Tx (n)

    f(i, j) - jesteśmy w stanie uzyskać j używając tylko liczb A[:i+1]

    f(i, j) = f(i-1, j) or f(i-1, j-A[i])

    """


def nwp(a, b):
    """
    Najdłuższy wspólny podciąg. NWP.
    Dane dwa ciągi liczb A i B.

    Oba są n-elementowe chcemy znaleźć podciąg który ma największą długość
    taki, że występuje on w A i w B.
    !Podciąg nie musi być spójny.!

    F(x,y) -> najdłuższy wspólny podciąg jeśli rozważamy A[:x] i B[:y]
    F(x,y) = max( (F(x-1, y) , F(x, y-1),  F[x-1][y-1] + 1 tylko jeśli A[x] = A[y])


    """


def npr(A):
    """
    Najdłuższy podciąg rosnący.
    Talica A liczb naturalnych n-elementowa.
    Chcemy znaleźć taki podciąg A który ma maks długość i w którym elementy są ułożone rosnąco.
    Podciąg nie musi być spójny.

    f(k,i) -> wykorzystując pierwszych k elementów z A
              jaki jest najmniejszy element w rosnącym podciągu o długości i

    f(k, 0) = +inf
    f(k, i) = A[j],   A[i] > f(j, i-1)
    f(k,i)  = f(k-1, i), f(k-1, i) < A[i]

    żeby nlogn
    Elementy ułożone rosnąco i wyszukiwanie binarnie.

                  -
    A = [2, 7, 3, 5, 1, 7]
    pierwszy elementy większy od 5 w B

    B = [2, 3, inf, fin,  inf, inf]

    B[i] -> najlepszy ciąg i elementowy


    """
    n = len(A)


def macierze(A):
    """
    Mnożenie macierzy
    tablica macierzy A - n macierzy
    Chcemy pomnoży te n macierzy
    Mamy podane ich wymiary. -> (wo, w1), (w1, w2), (w2, w3), ... (wn-1, wn)
    w0 ... wn

    Mnożenie macierzy jest łączne.
    Różnie nawiasy -> różny czas.
    Możenie macierzy (wo, w1) (w1, w2) ~ O(w*w1*w2)

    Znajdź takie pogrupowanie żeby pomnożyć macierze jak najszybciej.



    a - początek przedziału, b -koniec przedziału
    F[a][b] - sprawdzamy każde możliwe podzielenie tego przedziału na dwie części
    f(a,b) - min podział f(a,u) + f(u, b) + w[a]*w[u]*w[b]
    (    )(  )
    a    u   b

    """
