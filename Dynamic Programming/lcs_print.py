
def solve(text1, text2):
    
        m = len(text1)
        n = len(text2)
        t = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    t[i][j] = t[i - 1][j - 1] + 1
                else:
                    t[i][j] = max(t[i][j - 1], t[i - 1][j])

        s = ""
        while m > 0 and n > 0:
            if text1[m-1] == text2[n-1]:
                s += text1[m-1]
                m -= 1
                n -= 1
            elif t[m-1][n] > t[m][n-1]:
                m -= 1
            else:
                n -= 1

        return s[::-1]

print( solve('AFGCKJH','ABDCEF'))