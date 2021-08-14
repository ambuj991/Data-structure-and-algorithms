#Given the root of a binary tree and an integer targetSum, return true if the tree has a 
# root-to-leaf path such that adding up all the values along the path equals targetSum
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def hasPathSum( root, targetSum):
        # dfs is ok and is a clean implementaiton
        # the problem is stop the precedure once we found the sum can be done
        if root is None: 
            return False
        target = targetSum - root.val
        if target == 0 and root.left is None and root.right is None: 
            return True
        if target !=0 and root.left is None and root.right is None: 
            return False
        return hasPathSum(root.left, target) or hasPathSum(root.right, target)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
target=int(input())
print(hasPathSum(root,target))

