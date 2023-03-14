class Node:
    def __init__(self) -> None:
        self.val = 0
        self.next = None


# uniform distribution [a,b]
# [2, 5] n = 3
# [2-3], [3,4] [4-5]
# [a, b]
# [0, b-a]
# [0, 3]
# [0-1, 1-2, 2-3]


def length(first: Node) -> int:
    p = first
    n = 0
    while p != None:
        n += 1
        p = p.next
    return n

# [2,     6] n=4
#  [  [2-3), [3, 4), [4, 5), [5, 6)]

def bucket_sort(first: Node, a: int, b: int) -> Node:
    n = length(first)
    if n == 0: return first

    buckets = [Node() for _ in range(n+1)]
    pointers = [buckets[i] for i in range(n+1)]

    p = first
    while p != None:
        # (val-a) [0,b-a]
        # (val-a)/(b-a) [0, 1]
        # (val-a)/(b-a) * [0, n]
        # int((val-a)/(b-a)) * [0, n]
        ind = int((p.val-a)/(b-a)*n)

        bucket_ptr = pointers[ind]
        bucket_ptr.val = p.val
        bucket_ptr.next = Node()
        bucket_ptr = bucket_ptr.next
        pointers[ind] = bucket_ptr




