from egzP5atesty import runtests 

# 2 1 5 6 2 3
def inwestor ( T ):
    n = len(T)
    M = 0

    for i in range(0, n):
        m = T[i]
        for j in range(i+1, n):
            m = min(m, T[j])
            M = max(M, (j-i+1)*m)

    return M

    #            
print(inwestor([2,1,5,6,2,3]))
runtests ( inwestor, all_tests=True )