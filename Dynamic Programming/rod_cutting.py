
def cutRod( price, n):
    t = [[0 for j in range(n+1)] for i in range(n+1)]
    
    length = [ i for i in range(1,n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if length[i-1] <=j:
                t[i][j] = max((price[i-1] + t[i][j- length[i-1]]), t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][n]

print( cutRod([1, 5, 8, 9, 10, 17, 17, 20],8))