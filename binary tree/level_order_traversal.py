# level order traversal or bft
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelOrderTraversal(root):

    queue = []
    queue.append(root)
 
    # loop till queue is empty
    while queue:
        curr = queue.pop(0)
 
        print(curr.data, end=' ')
 
        if curr.left:
            queue.append(curr.left)
 
        if curr.right:
            queue.append(curr.right)

root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)

print(levelOrderTraversal(root))


