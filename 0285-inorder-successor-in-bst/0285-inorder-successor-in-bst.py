# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':    
        def explore(node):
            if self.status == 1:
                return 
            if node.left:
                explore(node.left)
            if self.status == 0 :
                self.successor = node
                self.status = 1
                return
            if node.val == p.val:
                self.status = 0
            if node.right:
                explore(node.right)
        self.status = -1 #-1 means not found p, 0 means ready to found nearest successor, 1 means successor found
        self.successor = None
        explore(root)
        return self.successor