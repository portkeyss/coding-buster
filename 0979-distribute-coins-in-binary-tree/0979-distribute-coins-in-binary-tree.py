# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        def f(node):
            if node is None: return (0,0)
            a,b = f(node.left)
            c,d = f(node.right)
            overflow = b+d+node.val-1
            move = a+c+abs(overflow)
            return (move, overflow)

        return f(root)[0]