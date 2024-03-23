# mamy miasta
# jest sieć drogowa
# każda krawędź reprezentuje odległość między miastami
# mamy wybrane dwa miasta
# source i target
# trzeba przewięć z source do target pewien składnik A
#                 z target do source pewnien składnik B
# jeśli skłądniki znajdą się na mniej niż D to wybuch bomby atomowej
# nie mogą się minąć na krawędzi
# nie mogą się znależć mniej niż D kilometrów
# trik:
# stan podróży
# położenie ładunku A
# położenie ładunku B
# n^2 możliwych stanów
# trzeba skonstruować nowy graf ->
# graf stanów
# wierzchołek - para legalna
# krawędź - zmiana stanu
# sprawdzić czy istnieje ścieżka ze stanu początkowego do końcowego
# n - wierzchołków
# nie można zrobić flipa ie (u,v) -> (v,u)
# O(n^3 + n^4)

# graf w repr. macierzowej
# mamy wagę = 1 -> jeżeli jest krawędź
#             inf -> jeżeli nie ma krawędzi
# domknięcie przechodnie
# jeżeli jest ścieżka z A->D
# to w domnięciu przechodnim jest krawędź z A->D
# macierz sąsiedzctwa
# floyd-warshall


def transitive_closure(A):
    n = len(A)


def get_dist_matrix(A):
    n = len(A)

# graf skieowany ważony
# wagi dodatnie
# znajdź cykl o minimalnej sumie wag
#
