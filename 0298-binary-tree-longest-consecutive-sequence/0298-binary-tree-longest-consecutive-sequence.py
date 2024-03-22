# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.maxLen = 1
        def dfs(node, parentVal, curLen):
            if node is None:
                return
            if node.val == parentVal+1:
                curLen += 1
                self.maxLen = max(self.maxLen, curLen)
            else:
                curLen = 1
            dfs(node.left, node.val, curLen)
            dfs(node.right, node.val, curLen)
        dfs(root, -float('inf'), 0)
        return self.maxLen     