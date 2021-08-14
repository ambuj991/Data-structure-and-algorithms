import heapq 

def solve(A,B):
        largest=[]
        for i in A:
            if len(largest)<B:
                heapq.heappush(largest,i)
            else:
                heapq.heappushpop(largest,i)
        if (len(largest) < B):
            return None
        return largest

    
arr = list(map(int, input().split()))
print(solve(arr,2))