from collections import deque


def atomic_bomb(cities, s, t, max_dist):
    return exists_state_path(cities, (s, t), (t, s), max_dist)


def exists_state_path(cities, start, finish, max_dist):
    n = len(cities)
    min_dist = create_min_dist_matrix(cities)
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True

    while len(queue) > 0:
        state = queue.popleft()
        if state == finish:
            return True

        for a, b in state_neighbours(state, min_dist, cities, max_dist):
            if not visited[a][b]:
                visited[a][b] = True
                queue.append((a, b))
    return False


def create_min_dist_matrix(cities):
    n = len(cities)
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    for v in range(n):
        dist[v][v] = 0

    for v in range(n):
        for u, w in cities[v]:
            dist[v][u] = w

    for i in range(n):
        for v in range(n):
            for u in range(n):
                dist[v][u] = min(dist[v][u], dist[v][i] + dist[i][u])

    return dist


def state_neighbours(state, min_dist, cities, max_dist):
    a, b = state
    is_okay = lambda na, nb: min_dist[na][nb] < max_dist and (na, nb) != (b, a)

    for new_a, _ in cities[a]:
        for new_b, _ in cities[b]:
            if is_okay(new_a, new_b):
                yield new_a, new_b

    for new_b, _ in cities[b]:
        if is_okay(a, new_b):
            yield a, new_b

    for new_a, _ in cities[a]:
        if is_okay(new_a, b):
            yield new_a, b
