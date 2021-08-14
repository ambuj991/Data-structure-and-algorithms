from collections import deque
# no need to create a class when using deque below i have done formality

class stack:
    def __init__(self):
        self.container=deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def isempty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

s=stack()
s.push(1)
s.push(3)
s.push(4)
s.push(5)
print(s.peek())
print(s.pop())
print(s.size())