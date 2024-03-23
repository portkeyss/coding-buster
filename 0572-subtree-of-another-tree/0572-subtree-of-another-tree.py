# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isEqual(a, b):
            if a is None:
                return b is None
            if b is None:
                return a is None
            return a.val == b.val and isEqual(a.left, b.left) and isEqual(a.right, b.right)

        return isEqual(s,t) or (s.left and self.isSubtree(s.left, t)) or (s.right and self.isSubtree(s.right, t))