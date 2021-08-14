class Node:
 
    # Utility function to create new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def isMirror(root1, root2):
    # If both trees are empty, then they are mirror images
    if root1 is None and root2 is None:
        return True
 
    """ For two trees to be mirror images,
        the following three conditions must be true
        1 - Their root node's data must be same
        2 - left subtree of left tree and right subtree
          of the right tree have to be mirror images
        3 - right subtree of left tree and left subtree
           of right tree have to be mirror imageso
    """
    if (root1 is not None and root2 is not None):
        if root1.data == root2.data:
            return (isMirror(root1.left, root2.right)and
                    isMirror(root1.right, root2.left))
 
    # If none of the above conditions is true then root1
    # and root2 are not mirror images
    return False
 
def isSymmetric(root):
    return isMirror(root, root)

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
print("Symmetric" if isSymmetric(root) == True else "Not symmetric")