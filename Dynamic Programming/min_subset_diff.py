# minimum subset sum difference

import sys
 

def findMin(a, n):
     
    su = 0
     
    # Calculate sum of all elements
    su = sum(a)
 
    # Create an 2d list to store
    # results of subproblems
    dp = [[0 for i in range(su + 1)]
             for j in range(n + 1)]
 
    # Initialize first column as true.
    # 0 sum is possible
    # with all elements.
    for i in range(n + 1):
        dp[i][0] = True
         

    # Fill the partition table in
    # bottom up manner
    for i in range(1, n + 1):
        for j in range(1, su + 1):
             
            
             
            # If i'th element is included
            if a[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - a[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

     
    # Initialize difference
    # of two sums.
    diff = sys.maxsize
 
    # Find the largest j such that dp[n][j]
    # is true where j loops from sum/2 t0 0
    for j in range(su // 2, -1, -1):
        if dp[n][j] == True:
            diff = su - (2 * j)
            break
             
    return diff
     
# Driver code
a = [ 3, 1, 4, 2, 2, 1 ]
n = len(a)
     
print("The minimum difference between "
      "2 sets is ", findMin(a, n))