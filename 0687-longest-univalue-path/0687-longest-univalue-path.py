# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            pathNodes = 1
            depth = 1
            if node.left and node.left.val==node.val:
                pathNodes += l
                depth = max(depth, 1+l)
            if node.right and node.right.val==node.val:
                pathNodes += r
                depth = max(depth, 1+r)
            self.res = max(self.res, pathNodes-1)
            return depth
        
        self.res = 0
        dfs(root)
        return self.res