def generate_subsets(n, p, array):
    if p == n:
        print(array)
    else:
        array[p] = 0
        generate_subsets(n, p+1, array)
        array[p] = 1
        generate_subsets(n, p+1, array)

