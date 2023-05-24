from collections import deque


def bfs(graph):
    order = len(graph)
    queue = deque()
    visited = [False]*order

    queue.appendleft(0)
    visited[0] = True

    while len(queue) != 0:
        v = queue
        for i in range(order):
            pass



