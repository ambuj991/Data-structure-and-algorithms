# max sum path

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def maxPathSum(root) -> int:
        ans = float("-inf")

        def postorder(root):
            if not root:  return 0

            left_val, right_val = max(0, postorder(root.left)), max(0, postorder(root.right))
            nonlocal ans
            print(ans)
            ans = max(ans, (root.val + left_val + right_val))
            return max((root.val + left_val), (root.val + right_val))

        postorder(root)
        return ans

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(maxPathSum(root))

