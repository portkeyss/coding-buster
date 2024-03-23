"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        newNode = Node(insertVal)
        if head is None:
            head = newNode
            head.next = head
            return head
        l = head
        while l.next != head:
            if (l.val <= insertVal <= l.next.val) or (l.val > l.next.val and (insertVal >= l.val or insertVal <= l.next.val)):
                newNode.next = l.next
                l.next = newNode
                return head
            l = l.next
        l.next = newNode
        newNode.next = head
        return head