# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root is None:
            return []
        res = []
        to_delete = set(to_delete)
        
        def f(node, parent):
            if parent in to_delete and node.val not in to_delete:
                res.append(node)
            if node.left:
                f(node.left, node.val)
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                f(node.right, node.val)
                if node.right.val in to_delete:
                    node.right = None
        
        to_delete.add(0) # 0 is a helper node used as root's parent
        f(root, 0)
        return res