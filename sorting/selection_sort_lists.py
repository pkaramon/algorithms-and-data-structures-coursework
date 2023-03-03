class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next


def del_max(first: Node) -> Node:
    first = Node(None, first)
    p = first
    m = first
    while p.next != None:
        if m.next.key < p.next.key:
            m = p
        p = p.next
    


def sort_list(first: Node):
    result = None
    while first != None:
        max = del_max(first)
        result = Node(max.key, result)

# 1-> 3 -> 2 -> 7 -> 4
# 1-> 3 -> 2 -> 4   7
# 1-> 3 -> 2   4 -> 7
#  ...
