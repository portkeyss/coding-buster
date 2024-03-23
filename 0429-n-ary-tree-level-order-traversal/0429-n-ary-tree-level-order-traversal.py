"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return[]
        res = [[root.val]]
        q = [root]
        while q:
            t = []
            s = []
            for x in q:
                for y in x.children:
                    t.append(y)
                    s.append(y.val)
            q = t
            if s: res.append(s)
        return res  