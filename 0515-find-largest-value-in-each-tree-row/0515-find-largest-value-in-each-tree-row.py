# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        q = [root]
        res = []
        while q:
            t = []
            mx = -inf
            for node in q:
                mx = max(mx, node.val)
                if node.left:
                    t.append(node.left)
                if node.right:
                    t.append(node.right)
            res.append(mx)
            q = t
        return res