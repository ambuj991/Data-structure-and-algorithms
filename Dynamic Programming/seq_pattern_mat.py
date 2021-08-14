# sequence pattern matching  , aditya verma

def solve(a, b):
    m,n =len(a), len(b)
    t = [[0]*(n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1]==b[j-1]:
                t[i][j]= 1+t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    return t[-1][-1] == min(len(a), len(b))



a= input()
b= input()
print(solve(a, b))