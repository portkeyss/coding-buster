# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node):
            if node is None:
                return True
            leftIsUni = dfs(node.left)
            rightIsUni = dfs(node.right)
            if (node.left is None or node.left.val == node.val and leftIsUni) and (node.right is None or node.right.val == node.val and rightIsUni):
                self.count += 1
                return True
            return False
        dfs(root)
        return self.count