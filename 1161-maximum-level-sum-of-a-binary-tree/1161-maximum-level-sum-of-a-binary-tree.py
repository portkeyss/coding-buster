# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        d = 0
        p = [-inf, -1]
        while q:
            d += 1
            t = []
            sm = 0
            for a in q:
                sm += a.val
                if a.left:
                    t.append(a.left)
                if a.right:
                    t.append(a.right)
            if sm > p[0]:
                p = [sm, d]
            q = t
        return p[1]