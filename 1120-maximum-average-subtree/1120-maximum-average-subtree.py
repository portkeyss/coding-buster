# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.ans = 0
        def dfs(node): #return the sum and total count of nodes in this subtree stree rooted at node
            if node is None:
                return (0,0)
            leftSum, leftNodes = dfs(node.left)
            rightSum, rightNodes = dfs(node.right)
            sm = leftSum + node.val + rightSum
            ct = leftNodes + 1 + rightNodes
            self.ans = max(self.ans, sm/ct)
            return sm, ct
        dfs(root)
        return self.ans