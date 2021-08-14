# Minimum number of deletion in a string to make it a palindrome
class Solution:
    def min_del(self, s: str) -> int:
        s1=s[::-1]
        n=len(s)
        t = [[0]*(n+1) for i in range(n+1) ]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s1[i-1]==s[j-1]:
                    t[i][j] = 1+ t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        return len(s)-t[n][n]
S=Solution()
print(S.min_del('agbcba'))
                