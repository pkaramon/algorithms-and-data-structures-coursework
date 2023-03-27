def parent(i): return (i0) // 2
def left(i)  : return 2*i + 1
def right(i) : return 2*i + 2


def heapify(T, i, size):
    if i == 0: return
    p = parent(i)
    if T[i] > T[p]:
        T[i], T[p] = T[p], T[i]
        heapify(T, p, size)


def insert(T, el):
    n = len(T)
    T.append(el)
    heapify(T, n, n+1)

def f(x:int, y:str, z:bool) -> str:
    pass