# nearest greater to right

def nearestGreaterToRight(arr):
  stack = []
  result = []

  for i in range(len(arr)-1, -1, -1):
    if len(stack)==0:
      result.append(-1)

    else:
      while(not len(stack)==0 and arr[i] > stack[-1]):
        stack.pop()
      if len(stack)==0:
        result.append(-1)
      else:
        result.append(stack[-1])
    stack.append(arr[i])
    
  result.reverse()
  return result

#arr= [11, 13, 21, 3]       21 13 

arr =list(map(int,input().split()))
print(nearestGreaterToRight(arr))