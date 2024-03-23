# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = Counter()
        def dfs(node):
            if node is None: return
            freq[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        maxFreq = max(freq.values())
        return [k for k,v in freq.items() if v==maxFreq]