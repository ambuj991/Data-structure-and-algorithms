# longest common subsequence Memoization 
memo = [[-1 for i in range(1001)] for j in range(1001)]

def lcsM(X, Y, m, n):
  
    if m == 0 or n == 0:
       return 0
    if memo[m][n]!=-1:
        return memo[m][n]

    if X[m-1] == Y[n-1]:
       memo[m][n] = 1 + lcsM(X, Y, n-1, m-1)
       return memo[m][n]
    
    else:
        memo[m][n] = max(lcsM(X, Y, n-1, m), lcsM(X, Y, n, m-1))
        return memo[m][n]
  
  
# Driver program to test the above function
X = "abc"
Y = "def"
print("Length of LCS is ", lcsM(X , Y, len(X), len(Y)))