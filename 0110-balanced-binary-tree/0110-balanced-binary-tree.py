# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root)[0]
    
    def dfs(self, root):
        if not root:
            return (True,0)
        leftBalanced, leftDepth = self.dfs(root.left)
        rightBalanced, rightDepth = self.dfs(root.right)
        depth = 1 + max(leftDepth, rightDepth)
        if not leftBalanced or not rightBalanced:
            return (False, depth)
        if abs(leftDepth - rightDepth) > 1:
            return (False, depth)
        return (True, depth)