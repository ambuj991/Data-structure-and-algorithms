def subsetSum(A, sum):
 
    n = len(A)
    T = [[0 for x in range(sum + 1)] for y in range(n + 1)]

    for i in range(n + 1):
        T[i][0] = 1
    
    for i in range(1, n + 1):

        for j in range(1, sum + 1):
            if A[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = T[i - 1][j] + T[i - 1][j - A[i - 1]]
    
    return T[n][sum]

print(subsetSum([2,0,2],4))