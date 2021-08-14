# Minimum Number of Insertion and Deletion to convert String a to String b

class Solution:
    def min_num(self, word1: str, word2: str):
        m, n = len(word1), len(word2)
        t = [[0]*(n+1) for i in range(m+1) ]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1]==word2[j-1]:
                    t[i][j] = t[i-1][j-1] +1
                else:
                    t[i][j] =max( t[i-1][j], t[i][j-1] )
        lcs = t[m][n]

        return len(word1)-(lcs) ,len(word2)-(lcs)

s=Solution()
print('(insertion, deletion) =', s.min_num('heap','pea'))
