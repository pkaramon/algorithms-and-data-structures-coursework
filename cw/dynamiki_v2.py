"""
1. Czarny las

Ścinamy drzewa od 0 do n-1.
Każde drzewo ma jakąś wartość ci.
Nie można ściąć dwóch sąsiednich drzew.

F(i, true) = F(i-1, false) + ci
F(i, false) = max(F(i-1, true), F(i-1, false))

"""
import keyword


def black_forest(trees):
    n = len(trees)
    cut = [0] * n
    not_cut = [0] * n

    for i in range(1, n):
        cut[i] = not_cut[i-1] + trees[i]
        not_cut[i] = max(cut[i-1], not_cut[i-1])
    return max(cut[n-1], not_cut[n-1])

def black_forest_optim(trees):
    n = len(trees)
    cut = 0
    not_cut = 0

    for i in range(1, n):
        cut, not_cut = not_cut + trees[i], max(not_cut, cut)
    return max(cut, not_cut)


"""2. Głodna żaba
oś 0...n-1
a_i - wartość przekąski dla żaba
jak żaba stanie na a_i to zjada tą przekąskę

żaba skacze, koszt skoku z i do j kosztuje j-i,
ale jak stanie na a_i do dostaje tą energię
minimalna liczba skoków żeby do końca.

Tylko skoki w prawo.

F(i) - min ilość skoków
F(i,t) - minimalna liczba skoków niezbędna aby dotrzeć do końca 
         jeśli żaba stoi na poz i oraz ma t energii.
         
F(i,t) = min {
    (F(i+jump, t + a_i - jump) + 1)
    for jump in range(1, t+a_i+1)
}

F(i, 0) = +inf
"""

print(keyword.softkwlist)


"""3. 2d problem plecakowy
Mamy lista przedmiotów.
p1, ..., pn
Każdy przedmiot pi = (wartość, waga, wysokość)
Mamy złodzieja
W - max waga
H - max wysokość

T_i(x,y) - maksymalna wartość skradzionych przedmiotów spośród 0...i
           zajmujących wagę x i wysokość y

T(i, x, y) = max {
    T(i-1, x-w_i, y - h_i) + v_i <=> x>=w_i ^ y >= h_i ,
    T(i-1, x, y)
}
"""

"""4. Ścieżka w drzewie.

Mamy drzewo ukorzenione w t.
Każdy wierzchołek w drzewie ma wartość value(v), może być ujemna.
Chcemy znaleźć prosta ścieżkę o maksymalnej sumie wartość.

Dla każdego v in V, określamy mu maksymalną ścieżkę.
F(v) - długość maksymalnej ścieżki która zaczyna się w v i schodzi do podrzewa.
M(v) - długość maksymalnej ścieżki która przechodzi przez v

return => max(M(v) for v in V)

"""

"""5. Ładowanie promu

Prom ma dwa pasy.
Mamy KOLEJKĘ aut.
Wszystkie auto.

Auto może wjechać na lewy albo prawy pas, albo nie wjechać bo nie ma miejsce.
Długości samochodów. A
Długość promu.       L 

Ile może auto wjechać.

"""