# cave is [gold, [gold to open, cave]]
def mage(caves):
    return bellman_ford_caves(caves)


def bellman_ford_caves(caves):
    n = len(caves)
    dist = [float('-inf')] * n
    dist[0] = 0

    for _ in range(n - 1):
        for v, u, w in get_edges(caves):
            print('edge', v, u, w)
            if dist[u] < dist[v] + w:
                dist[u] = dist[v] + w

    return dist[n - 1]


def get_edges(caves):
    for i in range(len(caves)):
        cave = caves[i]
        gold = cave[0]
        for j in range(1, 4):
            gold_to_open, door = cave[j]
            if door != -1:
                yield i, door, gold - gold_to_open


xd = [
    [8, [6, 3], [4, 2], [7, 1]],
    [22, [12, 2], [21, 3], [0, -1]],
    [9, [11, 3], [0, -1], [7, -1]],
    [15, [0, -1], [1, -1], [0, -1]],
]
print(mage(xd))
