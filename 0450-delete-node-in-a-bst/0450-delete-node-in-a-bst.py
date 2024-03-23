# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root or root.val == key and not root.left and not root.right:
            return None
        
        def findNode(n, key):
            p = None
            while n.val != key:
                if n.val < key:
                    if n.right is None:
                        return (None,None)
                    else:
                        p = n
                        n = n.right
                elif n.val > key:
                    if n.left is None:
                        return (None, None)
                    else:
                        p = n
                        n = n.left
            return (p, n)
        
        def findPrev(node):
            p = node
            node = node.left
            while node.right:
                p = node
                node = node.right
            return (p, node)
        
        def findNext(node):
            p = node
            node = node.right
            while node.left:
                p = node
                node = node.left
            return (p, node)
        
        p, toDelete = findNode(root, key)
        if toDelete is None: return root
        
        while toDelete.left or toDelete.right:
            if toDelete.left:
                q, n = findPrev(toDelete)
            else:
                q, n = findNext(toDelete)
            toDelete.val = n.val
            p, toDelete = q, n
        
        if p.left == toDelete:
            p.left = None
        else:
            p.right = None   
        return root        