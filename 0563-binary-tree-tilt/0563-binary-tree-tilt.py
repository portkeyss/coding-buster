# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def f(node):
            if node is None:
                return (0,0)
            a, b = f(node.left)
            c, d = f(node.right)
            return (node.val+a+c, abs(a-c)+b+d)
        
        return f(root)[1]