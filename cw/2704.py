def dijkstra(M, s):
    # diagonal - zeros
    n = len(M)
    dist = [float('inf')] * n
    visited = [False] * n
    parent = [None] * n

    dist[s] = 0
    visited[s] = True

    while True:
        min_dist, ind = float('inf'), -1
        for i in range(n):
            if dist[i] < min_dist and not visited[i]:
                min_dist, ind = dist[i], i
        if ind == -1:
            return dist

        visited[ind] = True
        for v in range(n):
            if dist[v] > dist[ind] + M[ind][v]:
                dist[v] = dist[ind] + M[ind][v]
                parent[v] = ind

# graf acykliczny skierowany DAG
# najkrótsze ścieżki z s do wszystkich innych
# O(E) dla rzadkiego grafu
# sortowanie topologiczne
# zaczynam od źródła
# jedyne relaksakcje są między źródłem a następnikami
# relaksuje wszystkie krawędzie wychodzące z s
# robie relaksacje kolejne warstwy
# relaksacji warstawmi osiągalnych wierzchołków

# zbiór n walut
# mamy macierz k
# k[x][y] jednostka x daje nam ileś waluty y
# mamy sprawdzić czy istnieje w k cykl
# x1, x2, ..., xn, x1
# przechodząc przez wymiany dostaje więcej x1 niż zacząłem
# logarytmy
# minus
# belman ford
# sprawdzenie czy istnieje cykl

# mapa krajów w postaći Grafu G = (V, E)
# E - drogi
# graf ważony, krawędzie to drogi, waga to długość drogi
# po tym kraju jedzie autous alicja i bob
# jeżdzą na zmianę
# trasae wybiera alicja i alicja wybiera kto jedzie pierwszy
# alicja ma przejechać minimalną liczbę kilometrów
# mamy wierzchołek początkowy i końcowy
