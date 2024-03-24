# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node, p):
            v = 2*p+node.val
            if node.left is None and node.right is None:
                self.res += v
            if node.left:
                dfs(node.left, v)
            if node.right:
                dfs(node.right, v)
        dfs(root,0)
        return self.res