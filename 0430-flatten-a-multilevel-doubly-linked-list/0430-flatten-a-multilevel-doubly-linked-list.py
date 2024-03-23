"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        def f(h): #return the tail of this nested list
            l = tail = h # l is the pointer in the current level, tail dynamically points to the whatever being the latest node in any any level
            while l:
                tail = l
                nxt = l.next  
                if l.child:
                    childTail = f(l.child)
                    tail = childTail
                
                    l.next = l.child
                    l.child.prev = l
                    
                    childTail.next = nxt
                    if nxt:
                        nxt.prev = childTail
                    l.child = None
                l = nxt
            return tail
        f(head)
        return head