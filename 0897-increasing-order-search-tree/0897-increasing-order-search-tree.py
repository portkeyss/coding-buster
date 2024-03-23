# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def f(node):
            if node.left:
                h1, t1 = f(node.left)
                t1.right = node
                h = h1
                node.left = None
            else:
                h = node
            if node.right:
                h2, t2 = f(node.right)
                node.right = h2
                t = t2
            else:
                t = node
            return h,t
        return f(root)[0]