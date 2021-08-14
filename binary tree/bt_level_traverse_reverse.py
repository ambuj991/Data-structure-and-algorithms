class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def reverseLevelOrder(root):
    
    q = []
    q.append(root)
    ans = []
    while q:
        node = q.pop(0)
        if node is None:
            continue
          
        ans.insert(0,node.data)
          
        if node.right:
            q.append(node.right)
              
        if node.left:
            q.append(node.left)
              
    return ans
  
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
  
print("Level Order traversal of binary tree is",reverseLevelOrder(root))
