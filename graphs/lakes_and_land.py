from collections import deque

WATER = 0
LAND = 1
WATER_VISITED = 2
LAND_VISITED = 3


def find_lakes(matrix: list[list[int]]):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == WATER:
                print(expand(matrix, i, j))


def expand(matrix, i, j):
    """
    expands the water area at (i,j)
    @param matrix: map
    @param i:
    @param j:
    @return: -1 if water area is not a lake,
              number of water blocks if water area is a lake
    """
    n = len(matrix)
    matrix[i][j] = WATER_VISITED
    queue = deque()
    queue.append((i, j))
    lake_area = 1

    while len(queue) != 0:
        i, j = queue.popleft()
        for x, y in get_neighbours(i, j):
            if not is_in_bounds(x, y, n):
                return -1
            if matrix[x][y] == WATER:
                matrix[x][y] = WATER_VISITED
                queue.append((x, y))
                lake_area += 1
    return lake_area


def get_neighbours(i, j):
    return (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)


def is_in_bounds(i, j, n):
    return 0 <= i < n and 0 <= j < n

    #   1
    # 2 3 4
    #   6


matrix = [
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
find_lakes(matrix)
