"""Piotr Karamon

Aby znaleźć długość palindromu nieparzystej długość o środku w indeksie i 
"rozszerzamy" go maksymalnie czyli sprawdzamy czy kolejne elementy po lewej i po
prawej są sobie równe. Jeżeli nasz obecnie rozważany palindrom ma środek
wewnątrz innego większego palindromu to korzystamy z jego symetrii. I zaczynamy
rozszerzanie od promienia tego palindromu symetrycznego, uważając na to czy nie
wychodzimy poza większy palindrom. Jeżeli po rozszerzeniu nasz obecny palindrom sięga
dalej niż obceny palindrom "otaczający" to staje się nim. Na koniec
wyszukujemy max z promieni i zwaracamy długość tego palindromu.

Złożoność czasowa: O(n)
Złożoność pamięciowa: O(n)
"""

from zad1testy import runtests


def ceasar(s):
    n = len(s)
    if n == 0:
        return 0

    radii = [1] * n
    box_center, box_bound = 0, 0
    for i in range(n):
        radius = 1
        # używanie symetrii by zacząć od promienia > 1
        if i <= box_bound:
            bound_r = box_bound - i
            symmetric_r = radii[2 * box_center - i]
            radius = symmetric_r if symmetric_r < bound_r else bound_r

        # poszerzanie palindromu na tyle ile jest to możliwe
        while radius + i < n and i - radius > -1 and s[i + radius] == s[i - radius]:
            radius += 1

        # aktualizujemy palindrom otaczający by móc zaczynać od
        # większych promieni początkowych
        if i + radius - 1 > box_bound:
            box_center, box_bound = i, i + radius - 1

        radii[i] = radius
    return 2 * max(radii) - 1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ceasar, all_tests=True)
