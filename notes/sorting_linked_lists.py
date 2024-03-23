# sortowanie listy jednokierunkowych 
# przez scalanie
# L = |2 3 5 7 9| 1 3 | 8 10 15 | 7 9 | 2
# merge(l1, l2) ->  l3
# wycinamy serie naturalne
# getns(l1) -> l2 # wycięcie serii naturalnej
# genns(l1), getns(l2) scalamy i mergeujemy i wrzucamy na koniec listy
# concat(l1, l2)
# seria naturalna - seria która naturalnie jest juz posortowana 
# lista -> (head, tail)
#
# pseudocode
# getns(l1) -> l2
# concat(l1, l2) -> l
# merge(l1, l2) ->  l3
# empty(l) -> T/F 
# l -> lista
# 
# def sort(list):
#   while not empty(l):
#       a, b = getns(list), getns(list)
#       if empty(b):
#           return a
#       c = merge(a,b)
#       concat(list, c)
# 

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f'Node(val={self.val}, next={self.next})'


# 1 2 3,  4 6,  1 3 5 6
def sort(first):
    if first == None or first.next == None:
        return first

    head, tail = first, find_tail(first)
    while True:
        a, head = getns(head)
        b, head = getns(head)
        if b == None:
            return a
        c = merge(a, b)
        pass


def find_tail(first):
    if first == None:
        return None

    p = first
    while p.next != None:
        p = p.next
    return p


def getns(first):
    head, tail = first
    if head == None or head.next == None:
        return (head, tail), (None, None)

    p = head
    while p.next != None and p.next.val >= p.val:
        p = p.next
    newfirst = p.next
    p.next = None

    return (head, p), (newfirst, tail)


def merge(a, b):
    if a == None and b == None:
        return None

    ap, bp = a, b
    result = Node()
    result_last = result

    while ap != None and bp != None:
        if ap.val <= bp.val:
            result_last.next = ap
            result_last = result_last.next
            ap = ap.next
        else:
            result_last.next = bp
            result_last = result_last.next
            bp = bp.next

    result_last.next = ap if ap != None else bp

    return result.next


x = (Node(1, Node(3, Node(6, Node(8, Node(10, Node(11)))))))
y = (Node(2, Node(5, Node(7, Node(9, )))))
print(merge(x, y))
