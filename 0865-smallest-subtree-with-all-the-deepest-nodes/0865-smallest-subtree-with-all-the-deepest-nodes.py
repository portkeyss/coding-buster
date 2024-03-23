# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        parent = dict()
        q = []
        q.append(root)
        while q:
            t = []
            for tn in q:
                if tn.left:
                    t.append(tn.left)
                    parent[tn.left]=tn
                if tn.right:
                    t.append(tn.right)
                    parent[tn.right]=tn
            if t: q = t
            else: break

        while len(q)>1:
            t = set()
            for tn in q:
                t.add(parent[tn])
            q = t
        return list(q)[0]        
        