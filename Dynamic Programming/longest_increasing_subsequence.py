# longest increasing subsequence ( strictly )

def lis(arr):
    n = len(arr)
    dp = [1]*n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

nums = list(map(int, input().split()))
print(lis(nums))

# time = O(n^2)
# space = O(n)