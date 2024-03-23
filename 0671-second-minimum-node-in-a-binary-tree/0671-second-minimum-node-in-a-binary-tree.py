# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def f(node, p):
            if node.val > p:
                return node.val
            if not node.left:
                return 1<<31
            else:
                return min(f(node.left,p), f(node.right, p))
        res = f(root, root.val)
        return res if res < 1<<31 else -1