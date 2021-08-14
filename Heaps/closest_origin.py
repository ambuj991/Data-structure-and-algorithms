# kth closest to origin

from heapq import heappush, heappop
# maxheap
def kthClosestPoint(k: int, array: list):

    if k < 1:
        raise Exception('Invalid k')
    k_elements = []

    for x, y in array:
        dist = -(x**2+y**2)
        
        if len(k_elements) < k or k_elements[0][0] < dist:
            heappush(k_elements, (dist, x, y))
        if len(k_elements) > k:
            heappop(k_elements)

    return [[x, y] for dist, x, y in k_elements]

r=int(input())
c=int(input())
matrix=[]
for i in range(r):          
    a =[]
    for j in range(c):    
         a.append(int(input()))
    matrix.append(a)

x = int(input())
print(kthClosestPoint(x, matrix))

# O(n log k)