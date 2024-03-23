# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 1
        def dfs(node):
            if node is None: return (0,0)
            x1,y1 = dfs(node.left)
            x2,y2 = dfs(node.right)
            x = y = 1
            if node.left and node.left.val==node.val+1:
                x = max(x,1+x1)
            if node.right and node.right.val==node.val+1:
                x = max(x,1+x2)
            if node.left and node.left.val==node.val-1:
                y = max(y,1+y1)
            if node.right and node.right.val==node.val-1:
                y = max(y,1+y2)
            self.res = max(self.res, x+y-1)
            return (x,y)  
                
        dfs(root)        
        return self.res