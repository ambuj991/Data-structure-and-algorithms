# nearest smallest to left

def nsl(arr):
    result,stack=[],[]

    for i in range(len(arr)):
        if len(stack)==0:
            result.append(-1)
        else:
            while not len(stack)==0 and arr[i]<=stack[-1]:
                stack.pop()
            if len(stack)==0:
                result.append(-1)
            else:
                result.append(stack[-1])
        stack.append(arr[i])
    return result

arr=list(map(int,input().split()))
print(nsl(arr))

# 39 27 11 4 24 32 32 1 