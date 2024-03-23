import random

from linked_list import *


def selection_sort(first: Node):
    result = None
    p = first
    while p != None:
        t = result
        result, p = delete_max(p)
        result.next = t
    return result


def delete_max(first):
    first = Node(None, first)
    mp, p = first, first
    while p.next != None:
        if p.next.key > mp.next.key:
            mp = p
        p = p.next
    m = mp.next
    mp.next = mp.next.next
    m.next = None
    return m, first.next


def insertion_sort(first):
    if first == None:
        return None
    sort, unsort = first, first.next
    sort.next = None
    while unsort != None:
        sort = insert(sort, unsort.key)
        unsort = unsort.next
    return sort


def insert(first, key):
    first = Node(None, first)
    p = first
    while p.next != None:
        if p.next.key > key:
            n = Node(key, p.next)
            p.next = n
            return first.next
        p = p.next
    p.next = Node(key)
    return first.next


x = list(range(100))
random.shuffle(x)
ll = from_array(x)

print_linked_list(ll)
ll = insertion_sort(ll)
print_linked_list(ll)
