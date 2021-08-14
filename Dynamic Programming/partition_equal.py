# partition equal subset sum

def canPartition(nums) -> bool:
    
        n = len(nums)
        s = sum(nums)
        if s%2 != 0:
            return False
    
        target_sum = s//2
        T = [[False for x in range(target_sum + 1)] for y in range(n + 1)]
        for i in range(n + 1):
            T[i][0] = True
    
        for i in range(1, n + 1):

            for j in range(1, target_sum + 1):
                if nums[i - 1] > j:
                    T[i][j] = T[i - 1][j]
                else:
                    T[i][j] = T[i - 1][j] or T[i - 1][j - nums[i - 1]]
        return T[n][target_sum]


print(canPartition(([1,5,11,5])))