# Fewest Coins To Make Change

import sys
def findMinCoins(S, N):
    T = [0] * (N + 1)

    for i in range(1, N + 1):
        T[i] = sys.maxsize
        for c in range(len(S)):

            if i - S[c] >= 0:
                result = T[i - S[c]]
                if result != sys.maxsize:
                    T[i] = min(T[i], result + 1)
                

    return T[N] if T[N]!=sys.maxsize else -1

print( findMinCoins([1,2,5], 11))