""" Piotr Karamon
Generalnie to jest to dynamik
ale przyśpieszony z użyciem kolejki priorytetowej.


g(i) := minimalny koszt przejazdu do i-tego parkingu
        ale nie możemy używać wyjątku(przejazd o 2*T kilometrów)
f(i) := minimalny koszt przejazdu do i-tego parkingu

Czas: O(nlogn)
Pamięć: O(n)
"""

from math import inf
from zad9testy import runtests
import heapq


def min_cost(P, K, T, L):
    stops = list(zip(P, K))
    stops.append((0, 0))
    stops.append((L, 0))
    stops.sort(key=lambda parking: parking[0])

    n = len(stops)

    f = [inf for _ in range(n)]
    g = [inf for _ in range(n)]
    f[0] = 0
    g[0] = 0

    heap_g = [(0, 0)]
    heap_2g = [(0, 0)]
    heap_f = [(0, 0)]

    for i in range(1, n):
        (g_value, index) = heapq.heappop(heap_2g)
        while len(heap_2g) > 0 and stops[i][0] - stops[index][0] > 2 * T:
            (g_value, index) = heapq.heappop(heap_2g)
        if stops[i][0] - stops[index][0] <= 2 * T:
            f[i] = min(f[i], g_value + stops[i][1])

        calc_func(i, T, g, heap_g, stops)
        calc_func(i, T, f, heap_f, stops)

        heapq.heappush(heap_2g, (g[i], i))
        heapq.heappush(heap_2g, (g_value, index))

    return f[n - 1]


def calc_func(i, dist_limit, func, func_heap, stops):
    (func_value, index) = heapq.heappop(func_heap)

    while len(func_heap) > 0 and stops[i][0] - stops[index][0] > dist_limit:
        (func_value, index) = heapq.heappop(func_heap)

    if stops[i][0] - stops[index][0] <= dist_limit:
        func[i] = min(func[i], func_value + stops[i][1])
    heapq.heappush(func_heap, (func[i], i))
    heapq.heappush(func_heap, (func_value, index))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost, all_tests=True)
