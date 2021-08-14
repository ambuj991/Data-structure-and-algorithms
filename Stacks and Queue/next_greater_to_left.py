# next greater to left
# 1 3 2 4
def ngl(arr):
    result,stack=[],[]

    for i in range(len(arr)):
        if len(stack)==0:
            result.append(-1)
            
        else:
            while not len(stack)==0 and arr[i]>stack[-1]:
                stack.pop()
            if len(stack)==0:
                result.append(-1)
            else:
                result.append(stack[-1])
        stack.append(arr[i])
    return result
    
arr=list(map(int,input().split()))
print(ngl(arr))
