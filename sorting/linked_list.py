class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next

    def __repr__(self) -> str:
        return f'-> {to_array(self)}'


def print_linked_list(first):
    a = to_array(first)
    print('->', a)


def from_array(array):
    result = Node()
    p = result
    for el in array:
        n = Node(el)
        p.next = n
        p = n
    return result.next


def to_array(first):
    a = []
    while first != None:
        a.append(first.key)
        first = first.next
    return a
