# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def f(node):
            if node is None: return -inf,0
            l = f(node.left)
            r = f(node.right)
            return max(l[0],r[0],node.val+max(l[1],0)+max(r[1],0)),node.val+max(0,l[1],r[1])

        return f(root)[0]