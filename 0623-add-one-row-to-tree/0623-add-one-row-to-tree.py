# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        helper = TreeNode(0,root,None)
        def f(node,d):
            if d==1:
                l = TreeNode(val,node.left,None)
                r = TreeNode(val, None,node.right)
                node.left = l
                node.right = r
                return
            if node.left:
                f(node.left,d-1)
            if node.right:
                f(node.right,d-1)

        f(helper,depth)
        return helper.left