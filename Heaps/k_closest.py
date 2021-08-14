from heapq import heappush,heappop,heapify

def findClosestElements(arr, k, x):
    heap,res = [],[]
    for i in arr:
        heappush(heap,(abs(x-i),i))
    heapify(heap)
    for i in range(k):
        heappush(res,heappop(heap)[1])
    return (res)

arr=list(map(int,input().split()))
k = int(input())
x= int(input())

print(findClosestElements(arr,k,x))