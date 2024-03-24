# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.larger = 0
        def inorder(node):
            if node is None: return
            inorder(node.right)
            self.larger += node.val
            node.val = self.larger
            inorder(node.left)
        inorder(root)
        return root