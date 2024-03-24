# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        while q:
            t = []
            for node in q:
                if node.left:
                    t.append(node.left)
                if node.right:
                    t.append(node.right)
            if t==[]: return sum(tn.val for tn in q)
            q = t  