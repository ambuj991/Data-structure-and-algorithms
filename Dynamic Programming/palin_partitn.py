# palindrome partition
def isPalindrome(x):
    return x == x[::-1]
 
 
def minPalPartion(string, i, j):
    if i >= j or isPalindrome(string[i:j + 1]):
        return 0
    ans = float('inf')
    for k in range(i, j):
        count = (1 + minPalPartion(string, i, k)
            + minPalPartion(string, k + 1, j))
        ans = min(ans, count)
    return ans
 
 
string = "ab"
print(
"Min cuts needed for Palindrome Partitioning is ",
     minPalPartion(string, 0, len(string) - 1),
)