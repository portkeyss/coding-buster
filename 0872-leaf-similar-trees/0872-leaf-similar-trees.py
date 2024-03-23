# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def f(node):
            if not node.left and not node.right:
                l.append(node.val)
            if node.left:
                f(node.left)
            if node.right:
                f(node.right)
        l = []
        f(root1)
        l1 = l.copy()
        l = []
        f(root2)
        l2 = l
        return l1==l2