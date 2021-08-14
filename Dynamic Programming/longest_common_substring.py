def longest_common_substring(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
    res = 0
    L = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
                res = max(res, L[i][j])
            else:
                L[i][j] =0
    return res

X = "ABC"
Y = "BABA"
print("Length of longest_common_substring is ", longest_common_substring(X, Y))