# nearly sorted array or k sorted array

from heapq import heapify,heappop,heappush
def sort_k(arr, n, k):

    heap = arr[:k + 1]

    heapify(heap)

    target_index = 0
    for rem_elmnts_index in range(k + 1, n):
        arr[target_index] = heappop(heap)
        heappush(heap, arr[rem_elmnts_index])
        target_index += 1
 
    while heap:
        arr[target_index] = heappop(heap)
        target_index += 1
    return arr

arr = list(map(int, input().split()))
print(sort_k(arr,len(arr),3))