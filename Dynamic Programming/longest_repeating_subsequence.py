# Longest repeating subsequence

def solve(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
    L = [[0]*(n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1] and i!=j :
    
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
  
    return L[m][n]

A=input()

print( solve(A,A))