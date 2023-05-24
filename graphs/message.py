from collections import deque


def message(friends: list[(int, int)], n: int):
    graph = create_graph(friends, n)

    visited = [0] * n
    current = deque()
    next = deque()
    visited[0] = True
    current.append(0)

    day, max_wave_length = 0, 0
    while len(current) > 0:
        day += 1
        max_wave_length = max(max_wave_length, len(current))
        process_current_wave(current, graph, next, visited)
        next, current = current, next
    return day, max_wave_length


def process_current_wave(current, graph, next, visited):
    while len(current) > 0:
        v = current.popleft()
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                next.append(u)


def create_graph(friends, n):
    graph = [[] for _ in range(n)]
    for a, b in friends:
        graph[a].append(b)
        graph[b].append(a)
    return graph


print(message([]))
