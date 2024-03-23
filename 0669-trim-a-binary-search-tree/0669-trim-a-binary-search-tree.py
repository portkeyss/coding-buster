# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def f(node):
            if node is None: return None
            if node.val<low:
                return f(node.right)
            if node.val>high:
                return f(node.left)
            l=f(node.left)
            r=f(node.right)
            node.left=l
            node.right=r
            return node
        return f(root)