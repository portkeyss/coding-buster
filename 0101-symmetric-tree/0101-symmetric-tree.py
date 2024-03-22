# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.areSymmetric(root.left, root.right)
    
    def areSymmetric(self, l, r):
        if l is None:
            return r is None
        if r is None:
            return False
        if l.val != r.val:
            return False
        return  self.areSymmetric(l.left, r.right) and self.areSymmetric(l.right, r.left)
        