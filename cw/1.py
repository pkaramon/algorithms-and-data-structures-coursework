# tablica posortowana
# i,j taka że T[i] + T[j] = x
# T[j] = x - T[i]
# search for T[j] using binary search
# x = 11
# O(nlogn)
# 2 3 5 9 11 13 17 19
# i                 j
# T[i] + T[j] < x -> move j to left
# T[i] + T[j] > x -> move i to right


def findij(A, x):
    i, j = 0, len(A) -1
    while i!=j:
        if A[i] +  A[j] < x:
            j -= 1
        elif A[i] + A[j]  < x:
            i += 1
        else:
            return True
    return False

# dowolne liczby - 2 3 5 9 11 2 | 2 13 2 17 2 19 2 
# lider ciąg - taki element który występuję więcej niż ceil(n/2) razy
# 2 3 5 9 11 2 | 2 13 2 17 2 19 2 
# jeżeli tablica miała lidera a usunąłem dwa różne elementy to tablica nadal ma lidera
# i jest on taki sam
# będziemy się poruszać po tablicy
# zakładamy, że liderem jest pierwszy element
# idziemy dalej 
# potencjalny_lider, ile_razy_wystąpił
# lider -> +1
# nie lider -> -1
# counter < 0 -> nie lider
# 

# 1 2 2 2 3 7 1 2 3 4 9 1 2 2
def find_leader(A):
    n = len(A)
    if n == 0: return None
    leader, counter = A[0], 1

    for i in range(1, len(A)):
        counter += 1 if A[i] == leader else -1
        if counter < 0:
            leader, counter = A[i], 1
    
    counter = 0
    for x in A:
        counter += 1 if x == leader else 0
    return leader if counter > n//2 else None

# ZADANIE domowe
# jak sprawdzić czy jest pseudolider (co najmniej 1/3 elementów)?

# mamy ciąg przedziałów
# Dane = [(a,b), (a,b), (a,b), (a,b), ...]
# żaden początek i koniec nie pokrywają się
# znaleźć taki przedział który zawiera najwięcej przedziałów w całośći
# sortujemy punkty (2n) 
# dla każdego końca możemy policzyć liczbę która = ile jest przedziałów które
# kończą się na lewo od tego puntku
# dla każdego początku liczbymy ile przedziałów 

# dla każdego końca -> ile jest końców do tej pory (f)
# dla każdego początku -> ile przedziałów zaczyna się na lewo od tego początku (g)
# dla każego przedziału (np. A) g(A) - f(A) = 3
# 
# np. g(c) - f(c) =  2

# sortowanie listy jednokierunkowych 
# przez scalanie
# L = |2 3 5 7 9| 1 3 | 8 10 15 | 7 9 | 2
# merge(l1, l2) ->  l3
# wycinamy serie naturalne
# getns(l1) -> l2 # wycięcie serii naturalnej
# genns(l1), getns(l2) scalamy i mergeujemy i wrzucamy na koniec listy
# concat(l1, l2)
# seria naturalna - seria która naturalnie jest juz posortowana 
# lista -> (head, tail)
#
# pseudocode
# getns(l1) -> l2
# concat(l1, l2) -> l
# merge(l1, l2) ->  l3
# empty(l) -> T/F 
# l -> lista
# 
# def sort(list):
#   while not empty(l):
#       a, b = getns(list), getns(list)
#       if empty(b):
#           return a
#       c = merge(a,b)
#       concat(list, c)
# 

# tablica posortowana
# i,j taka że T[i] + T[j] = x
# T[j] = x - T[i]
# search for T[j] using binary search
# x = 11
# O(nlogn)
# 2 3 5 9 11 13 17 19
# i                 j
# T[i] + T[j] < x -> move j to left
# T[i] + T[j] > x -> move i to right


def findij(A, x):
    i, j = 0, len(A) -1
    while i!=j:
        if A[i] +  A[j] < x:
            j -= 1
        elif A[i] + A[j]  < x:
            i += 1
        else:
            return True
    return False

# dowolne liczby - 2 3 5 9 11 2 | 2 13 2 17 2 19 2 
# lider ciąg - taki element który występuję więcej niż ceil(n/2) razy
# 2 3 5 9 11 2 | 2 13 2 17 2 19 2 
# jeżeli tablica miała lidera a usunąłem dwa różne elementy to tablica nadal ma lidera
# i jest on taki sam
# będziemy się poruszać po tablicy
# zakładamy, że liderem jest pierwszy element
# idziemy dalej 
# potencjalny_lider, ile_razy_wystąpił
# lider -> +1
# nie lider -> -1
# counter < 0 -> nie lider
# 

# 1 2 2 2 3 7 1 2 3 4 9 1 2 2
def find_leader(A):
    n = len(A)
    if n == 0: return None
    leader, counter = A[0], 1

    for i in range(1, len(A)):
        counter += 1 if A[i] == leader else -1
        if counter < 0:
            leader, counter = A[i], 1
    
    counter = 0
    for x in A:
        counter += 1 if x == leader else 0
    return leader if counter > n//2 else None

# ZADANIE domowe
# jak sprawdzić czy jest pseudolider (co najmniej 1/3 elementów)?

# mamy ciąg przedziałów
# Dane = [(a,b), (a,b), (a,b), (a,b), ...]
# żaden początek i koniec nie pokrywają się
# znaleźć taki przedział który zawiera najwięcej przedziałów w całośći
# sortujemy punkty (2n) 
# dla każdego końca możemy policzyć liczbę która = ile jest przedziałów które
# kończą się na lewo od tego puntku
# dla każdego początku liczbymy ile przedziałów 

# dla każdego końca -> ile jest końców do tej pory (f)
# dla każdego początku -> ile przedziałów zaczyna się na lewo od tego początku (g)
# dla każego przedziału (np. A) g(A) - f(A) = 3
# 
# np. g(c) - f(c) =  2

# sortowanie listy jednokierunkowych 
# przez scalanie
# L = |2 3 5 7 9| 1 3 | 8 10 15 | 7 9 | 2
# merge(l1, l2) ->  l3
# wycinamy serie naturalne
# getns(l1) -> l2 # wycięcie serii naturalnej
# genns(l1), getns(l2) scalamy i mergeujemy i wrzucamy na koniec listy
# concat(l1, l2)
# seria naturalna - seria która naturalnie jest juz posortowana 
# lista -> (head, tail)
#
# pseudocode
# getns(l1) -> l2
# concat(l1, l2) -> l
# merge(l1, l2) ->  l3
# empty(l) -> T/F 
# l -> lista
# 
# def sort(list):
#   while not empty(l):
#       a, b = getns(list), getns(list)
#       if empty(b):
#           return a
#       c = merge(a,b)
#       concat(list, c)
# 
