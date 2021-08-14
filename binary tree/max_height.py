class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def maxDepth(node):
    if node is None:
        return 0
    
    lDepth = maxDepth(node.left)
    rDepth = maxDepth(node.right)
    return 1+max(lDepth,rDepth)


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
 
 
print ("Height of tree is %d" %(maxDepth(root)))