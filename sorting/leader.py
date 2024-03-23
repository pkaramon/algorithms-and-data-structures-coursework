"""
given an array of number find its leader
a leader -> an element which occurs more than n//2

in a 3 element array a leader must occurs at at least twice
in a 4 element array a leader must occur at least three times

Let's consider the following:
assume the leader is T[0], and set counter = 1;
go through the array
if T[i] is not the leader -> counter -= 1
if T[i] is the leader     -> counter += 1
if counter < 0:
    change the leader
    reset the counter
"""

import random


def find_leader(array):
    n = len(array)
    if n == 0:
        return -1

    leader, counter = 0, 0
    for i in range(n):
        if array[leader] == array[i]:
            counter += 1
        else:
            counter -= 1
        if counter == 0:
            leader, counter = i, 1

    count = 0
    for i in range(n):
        if array[i] == array[leader]:
            count += 1

    return leader if count > n / 2 else -1


x = [2] * 101 + [random.randint(1, 10000) for _ in range(100)]
random.shuffle(x)
print(x[find_leader(x)])
