# stock span problem

def span(price):

    stockspan = []
    stack = [] # Creating an empty stack
    # Base case
    stockspan.append(1)
    stack.append(0)
    for i in range(1, len(price)):

      # Pop elements out of stack until either: 
      # 1) The stack gets empty
      #or 2) the price at stack top turns out to be larger than the price
      #at the current element
      while price[i] > price[stack[-1]]:
        stack.pop()

        if len(stack) == 0:
          break
      # Set the stockspan values.
      if len(stack) > 0:
          stockspan.append(i - stack[-1])
      else:
          stockspan.append(i + 1) 
      stack.append(i)
    return stockspan

arr =list(map(int,input().split()))
print(span(arr))