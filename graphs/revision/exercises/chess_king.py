"""
We are given a board nxn.
In [0,0] there is king he has to go to [n-1, n-1]
with minimal cost.
Each cell contains a value {0, 1, 2, 4, 5} representing the cost.

Obvious solution: Dijkstra. O(V^2)

But we can actually do it in a simple way using BFS.
Because BFS finds the shortest paths in the terms of the number of edges.
The idea is to "add artificial edges" to the graph.

"""
from collections import deque


def chess_king(board):
    n = len(board)

    queue = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    parent = [[None for _ in range(n)] for _ in range(n)]

    queue.append((0, 0, 0))
    visited[0][0] = True

    while len(queue) > 0:
        x, y, v = queue.popleft()
        if v != 0:
            queue.append((x, y, v - 1))
            continue

        if x == n - 1 and y == n - 1:
            print(parent)
            path = (construct_path(parent))
            print(path)
            print(sum(board[u][v] for u, v in path))

            return

        for a, b in neighbours(x, y, n):
            if not visited[a][b]:
                queue.append((a, b, board[a][b]))
                visited[a][b] = True
                parent[a][b] = (x, y)


def construct_path(parent):
    n = len(parent)
    x, y = n - 1, n - 1
    path = []
    while parent[x][y] is not None:
        path.append((x, y))
        x, y = parent[x][y]
    path.reverse()
    return path


def neighbours(x, y, n):
    for o_x in (-1, 0, 1):
        for o_y in (-1, 0, 1):
            a, b = x + o_x, y + o_y
            if (a, b) != (x, y) and 0 <= a < n and 0 <= b < n:
                yield a, b


chess_king([
    [0, 2, 2, 3],
    [2, 5, 2, 3],
    [1, 9, 4, 3],
    [7, 1, 1, 1]
])
