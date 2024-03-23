"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def f(r,c,n):
            if n == 1:
                return Node(grid[r][c],1,None,None,None,None)
            tl = f(r,c,n//2)
            tr = f(r,c+n//2,n//2)
            bl = f(r+n//2, c, n//2)
            br = f(r+n//2, c+n//2, n//2)
            if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
                return Node(tr.val, 1, None,None, None, None)
            return Node(tr.val, 0, tl, tr, bl, br)
        
        return f(0,0,len(grid))