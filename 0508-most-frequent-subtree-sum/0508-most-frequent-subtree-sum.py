# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.freq = Counter()
        def dfs(node):
            if node.left is None and node.right is None:
                self.freq[node.val] += 1
                return node.val
            sm = node.val
            if node.left:
                sm += dfs(node.left)
            if node.right:
                sm += dfs(node.right)
            self.freq[sm] += 1
            return sm
        
        dfs(root)
        mx = max(self.freq.values())
        return [x for x,v in self.freq.items() if v==mx]