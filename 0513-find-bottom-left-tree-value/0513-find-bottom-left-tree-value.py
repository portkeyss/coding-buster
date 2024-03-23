# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = None
        q = [root]
        while q:
            res = q[0].val
            t = []
            for x in q:
                if x.left:
                    t.append(x.left)
                if x.right:
                    t.append(x.right)
            q = t
        return res