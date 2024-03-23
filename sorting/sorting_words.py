def counting_sort(elements, k, key=lambda x: x):
    n = len(elements)
    counts = [0] * k
    for i in range(n):
        counts[key(elements[i])] += 1
    for i in range(1, k):
        counts[i] += counts[i - 1]
    output = [0] * n

    for i in range(n - 1, -1, -1):
        x = key(elements[i])
        output[counts[x] - 1] = elements[i]
        counts[x] -= 1

    return output


def counting_sort_word(elements, nth):
    n = len(elements)
    counts = [0] * 27
    for i in range(n):
        x = ord(elements[i][nth]) - 96 if nth < len(elements[i]) else 0
        counts[x] += 1

    for i in range(1, 27):
        counts[i] += counts[i - 1]
    output = [0] * n

    for i in range(n - 1, -1, -1):
        x = ord(elements[i][nth]) - 96 if nth < len(elements[i]) else 0
        output[counts[x] - 1] = elements[i]
        counts[x] -= 1

    return output


def sort_words(words):
    max_length = 0
    for w in words:
        max_length = max(max_length, len(w))

    for i in range(max_length - 1, -1, -1):
        words = counting_sort_word(words, i)
    return words


words = ['ja', 'tim', 'zaz', 'cat', 'bob', 'hit', 'peter',
         'unix', 'crabs', 'spongebob', 'sponge', 'dog', 'raccoon', 'panda']

words = sort_words(words)
print(words)
