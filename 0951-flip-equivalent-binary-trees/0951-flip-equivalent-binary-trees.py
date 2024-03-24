# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def f(node1, node2):
            if node1 is None: return node2 is None
            if node2 is None: return False
            if node1.val != node2.val: return False
            return f(node1.left, node2.left) and f(node1.right, node2.right) or f(node1.left, node2.right) and f(node1.right, node2.left)
             
        return f(root1, root2)