from collections import deque


# checking if graph is bipartite
# graph is represented by a matrix nxn matrix

def is_bipartite(graph):
    n = len(graph)
    colors = [0 for _ in range(n)]
    for v in range(n):
        if colors[v] == 0:
            if not visit(graph, v, 1, colors):
                return False
    return True


def visit(M, v, col, colors):
    n = len(M)
    colors[v] = col
    c = 2 if col == 1 else 1
    for u in range(n):
        if M[v][u]:
            if colors[u] == 0:
                ret = visit(M, u, c, colors)
                if not ret:
                    return False
            elif colors[u] != c:
                return False
    return True


# zliczanie spójnych składowych

def count_components(G):
    n = len(G)
    visited = [False] * n
    n_comp = 0
    for v in range(n):
        if not visited[v]:
            n_comp += 1
            visited[v] = True
            visit(G, v, visited)
    return n_comp


def bfs_visit(G, v, visited):
    q = deque()
    visited[v] = True
    q.append(v)

    while len(q) != 0:
        u = q.popleft()
        visited[u] = True
        for p in G[u]:
            if not visited[p]:
                visited[p] = True
                q.append(p)


def visit(G, v, visited):
    for u in G[v]:
        visited[u] = True
        visit(G, u, visited)


def first_unvisited(G, visited):
    for i in range(G):
        if visited[i] == False:
            return i
    return -1


# składowe spojne, kolorowanie grafu

# checking if graph has a cycle of length 4
# pairs of V

# stacje nadawcze usuwanie
# chce to tak zrobić 
# mamy sieć reprezentwoaną jako grapf
# chcemy usuwać krawędzie tak żeby graf nie był nigdy nie spójny 
# chcemy usuwać wierdzchołki i jego krawędzie
# graf - stacje bazowe

# rozpinamy graf dfs który tworzy drzewo
# usuwamy liście
# listy sąsiedzctwa
# kolejność usuwania


def telecom(G):
    n = len(G)
    result = []
    visited = [False] * n
    dfs_visit(G, 0, visited, result)
    return result


def dfs_visit(G, s, visited, result):
    visited[s] = True
    for u in G[s]:
        if not visited[u]:
            dfs_visit(G, u, visited, result)
    result.append(s)

# szachownica nxn
# w każdym polu jest koszt {1,2,3,4,5}
# w [0, 0] jest król
# ma przejść do [n-1, n-1] tak aby koszt by minimalnym
# tworzymy graf wierdzchołek ma 8 krawędzi
# 3 -> -> -> []
# |
# v
# []
# |V|=O(n^2)
# |E|=O(n^2)
# na końcu 5*O(n^2)
