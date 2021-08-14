# palindrome partition
t = [[-1]*(100) for i in range(100)]
def isPalindrome(x):
    return x == x[::-1]
 
 
def minPalPartion(string, i, j):
    if i >= j or isPalindrome(string[i:j + 1]):
        return 0
    if t[i][j]!= -1:
        return t[i][j]
    t[i][j] = float('inf')
    for k in range(i, j):
        count = (1 + minPalPartion(string, i, k)
            + minPalPartion(string, k + 1, j))
        t[i][j] = min(t[i][j], count)
    return t[i][j]
 
 
string = input()
print(
"Min cuts needed for Palindrome Partitioning is ",
     minPalPartion(string, 0, len(string) - 1),
)