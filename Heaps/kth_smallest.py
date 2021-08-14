
import heapq

def kthSmallest(iterable, k):
    smallest = []
    heapq.heapify(smallest)
    for value in iterable:
        if (len(smallest) < k):
            heapq.heappush(smallest, -value)
        else:
            heapq.heappushpop(smallest, -value)
    if (len(smallest) < k):
        return None
    return -smallest[0]

arr = list(map(int, input().split()))
print(kthSmallest(arr,3))
