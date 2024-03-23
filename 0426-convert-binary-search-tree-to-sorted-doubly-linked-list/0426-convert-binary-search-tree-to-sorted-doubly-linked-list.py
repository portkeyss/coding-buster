"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        def rearrange(node):
            first = node
            last = node
            if node.left is not None:
                leftFirst, leftLast = rearrange(node.left)
                leftLast.right = node
                node.left = leftLast 
                first = leftFirst
            if node.right is not None:
                rightFirst, rightLast = rearrange(node.right)
                rightFirst.left = node    
                node.right = rightFirst
                last = rightLast
            return first,last
        first, last = rearrange(root)
        first.left = last
        last.right = first
        return first