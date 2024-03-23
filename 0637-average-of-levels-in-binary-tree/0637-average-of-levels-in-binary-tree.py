# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        l = [root]
        res = []
        while l:
            sm = 0
            t = []
            for tn in l:
                sm += tn.val
                if tn.left:
                    t.append(tn.left)
                if tn.right:
                    t.append(tn.right)
            res.append(sm/len(l))
            l = t
        return res