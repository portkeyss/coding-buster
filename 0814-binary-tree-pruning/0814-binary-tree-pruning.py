# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def f(node):
            if node is None: return False
            l=f(node.left)
            r=f(node.right)
            if l is False:
                node.left = None
            if r is False:
                node.right = None
            if l or r or node.val==1:
                return True
            else:
                return False
        helper = TreeNode(val=1,left=root)
        f(helper)
        return helper.left