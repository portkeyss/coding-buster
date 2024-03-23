# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        def f(node):
            if node is None: return 0
            return f(node.left)+f(node.right)+node.val
        sm = f(root)
        if sm%2==1: return False
        def g(node):
            if node is None: return 0
            p = g(node.left)+g(node.right)+node.val
            if p==sm//2 and node!=root:
                self.res = True
            return p
        self.res = False
        g(root)
        return self.res