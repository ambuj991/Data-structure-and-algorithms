# count the number of subset with given  difference

def subsetdiff (A,  diff):
    target_sum = (sum(A) + diff) //2
    if A==0 or target_sum%2!=0:
        return 0

    n = len(A)

    T = [[0 for x in range(  target_sum+ 1)] for y in range(n + 1)]

    for i in range(n + 1):
        T[i][0] = 1
    
    for i in range(1, n + 1):

        for j in range(1, target_sum+ 1):
            if A[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = T[i - 1][j] + T[i - 1][j - A[i - 1]]
    
    return T[n][target_sum]

print(subsetdiff ([1,1,1,1,1],3))