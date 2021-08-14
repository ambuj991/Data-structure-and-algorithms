# Coin change problem: Maximum number of ways

def solve (coins, N):
    t = [[0 for j in range(N+1)] for i in range(len(coins)+1)]
    
    for i in range(len(coins)+1):
        t[i][0] = 1
    
    for i in range(1, len(coins)+1):
        for j in range(1, N+1):
            if coins[i-1] > j:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = t[i-1][j] + t[i][j-coins[i-1]]
    
    return t[-1][-1]




coins = list(map(int, input().split()))
N = int(input())
print(solve(coins, N))