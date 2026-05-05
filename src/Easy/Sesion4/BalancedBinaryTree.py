"""

A balanced binary tree in alture means that the difference between the subtress are 0 or 1

Un árbol está balanceado cuando, en cada nodo,
la diferencia de alturas entre su subárbol izquierdo y derecho no es mayor que 1.


"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):

        def height(node):

            if not node:
                return 0

            left = height(node.left)
            if left == -1:
                return -1

            right = height(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return height(root) != -1


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)

print(Solution().isBalanced(root=root))