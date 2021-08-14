# remove adjacent duplicates
# Input: "abbaca"
# Output: "ca"

def removeDuplicates(S):
        stack=[]
        for i in S:
            if stack and i==stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

print(removeDuplicates('abbaca'))