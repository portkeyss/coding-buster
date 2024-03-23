# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        def f(node):
            if k-node.val in s: return True
            s.add(node.val)
            if node.left and f(node.left) or node.right and f(node.right):
                return True
            return False
        return f(root)