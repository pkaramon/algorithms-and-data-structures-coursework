# ścieżka Hamiltona
# w DAGu
# znaleźć lub stwierdzić że nie istnieje

# sortowanie topologiczne
# po posortowaniu po między i a i+1 musi istnieć ścieżka
# modulo corner case'y XD


# Formuła logiczna
# zmienne logiczne
# nie, i, lub - operator
# (-p v -q) ^ (~r v s) ^ (~s v q)
# 2CNF - max 2 zmienne
# (p=>-q) ^ (r => s) ^ (s => q)
# => - krawędź skierowana
# silnie wspólne składowe
# jeśli jedna 1 to kolejne 1
# jeśli zero to kolejne 0, bo byłaby sprzeczność
# silnie wspólna składowa -> jedna zmienna
# graf spójnych składoweych
#
# próbujemy 1 od "lewej" strony
# jeśli kolizja to 0
# itd.


# mamy graf skierowany nie koniecznie acykliczny
# mówimy, że v jest dobrym początkiem, jeżeli z tego
# wierzchołka osiągalne są wszystkie inne wierzchołki
#
# silnie wspólne składowe -> znikają cykle
# sortujemy topologicznie
# i wierzchołek z pierwszego
# musi być ścieżka z niego po kolei przez wszystkie



# znaleźć cykl Eulera
# graph - matrix
# result - [] by default

def dfs_visit(M, v, cycle):
    n = len(M)
    for u in range(n):
        if M[v][u]:
            M[v][u] = False
            M[u][v] = False
            dfs_visit(M, u, cycle)
    cycle.append(v)


def find_euler_cycle(M):
    M = [row[:] for row in M]
    cycle = []
    dfs_visit(M, 0, cycle)
    return cycle[::-1]


# mamy przewodnika turytycznego
# który chce przewieźć k turystyów z miasta S do miasta T
# w kraju są drogi
# przesiadki : (a, b, c) -> a, b - miasta c - pojemność
# a-skąd
# b-dokąd
# c-pojemność
# przewieźć turystów z jak najmniejszą ilość grup
# ala algorytm dijkstry


# liczba trójek * logarytm(największa pojemność)
# log(max_waga)*(rozmiar grafu)
# n - rozmiar danych
# n * log(w)
# n * log(w) -> n*n
# 2n - bitów
#
# binary search an pojemności

# wyszukiwać binarnie po wagach a nie po zakresie wag
# i na tym odpalamy wyszukiwanie połówkowe
# pesymistyczna nlogn
# jak są w tym samym zbiorze



# inaczej - bez binary search
# maksymalne drzewo rozpinające
#


# binary search na liczbie osób w grupie
# mamy 30 osób
# próbujemy 15
#  8
# ...


# znajdowanie mostów w grafie!

# zadanie domowe
# graf skierowany
# mówimy, że wierzchołek jest uniwersalnym ujściem jeśli
# z każdego innego wierzchołka istnieje krawędź do ujścia
# a z ujścia nie ma ścieżki do niczego

# graf repr. macierzowa
# czy istnieją uniwersalne ujście
# zrób w O(V)
