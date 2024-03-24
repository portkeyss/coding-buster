# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        covered = set()
        def f(node, parent=None):
            if not node:
                return
            f(node.left, node)
            f(node.right, node)
            if (not parent and node not in covered) or (node.left and node.left not in covered) or (node.right and node.right not in covered):
                self.res += 1
                covered.add(node)
                if parent:
                    covered.add(parent)
                if node.left:
                    covered.add(node.left)
                if node.right:
                    covered.add(node.right)
        f(root)
        return self.res