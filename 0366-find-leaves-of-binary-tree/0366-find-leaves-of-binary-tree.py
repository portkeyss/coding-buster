# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        removed = set()
        parent = dict()
        leaves = set()
        def dfs(node):
            if node.left is None and node.right is None:
                leaves.add(node)
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)
        dfs(root)

        res = []
        while leaves:
            res.append([leaf.val for leaf in leaves])
            removed |= leaves
            candidates = set()
            for leaf in leaves:
                if leaf in parent:
                    candidates.add(parent[leaf])
            leaves.clear()
            for candidate in candidates:
                if (candidate.left is None or candidate.left in removed) and (candidate.right is None or candidate.right in removed):
                    leaves.add(candidate)
        return res