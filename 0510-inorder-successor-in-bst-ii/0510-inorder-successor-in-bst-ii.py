"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            node = node.right
            while node:
                if node.left is None:
                    return node
                node = node.left
        else:
            while node.parent and node.parent.right==node:
                node = node.parent
            return node.parent    