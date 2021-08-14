# connect n ropes to minimize the cost

import heapq

def minCost(arr, n): 
    # Initializ result
    res = 0
    heapq.heapify(arr)
    # While size of priority queue
    # is more than 1
    while(len(arr) > 1):
         
        # Extract shortest two ropes from arr
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
         
        #Connect the ropes: update result
        # and insert the new rope to arr
        res += first + second
        heapq.heappush(arr, first + second)
         
    return res

     
lengths = list(map(int, input().split()))
size = len(lengths)
print("Total cost for connecting ropes is " +
          str(minCost(lengths, size)))


























# Time Complexity: O(nLogn), assuming that we use a O(nLogn) sorting algorithm. 
# Note that heap operations like insert and extract take O(Logn) time.
# Auxiliary Complexity: O(n). 
# The space required to store the values in min heap