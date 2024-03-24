# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        parent = defaultdict(lambda:-1)
        while q:
            t = []
            for treeNode in q:
                if treeNode.left:
                    t.append(treeNode.left)
                    parent[treeNode.left] = treeNode
                if treeNode.right:
                    t.append(treeNode.right)
                    parent[treeNode.right] = treeNode
            if t: q = t
            else: break
                
        q = set(q)
        while len(q)>1:
            t = set(parent[treeNode] for treeNode in q)
            q = t
        return  q.pop()      