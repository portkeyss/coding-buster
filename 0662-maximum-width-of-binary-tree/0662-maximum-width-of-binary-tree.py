# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = deque()
        q.append((root,0))        
        res = 0
        while q:
            q1 = deque()
            firstCol = q[0][1]
            while q:
                node, col= q.popleft()
                if node.left:
                    q1.append((node.left, 2*col))
                if node.right:
                    q1.append((node.right, 2*col+1))
            res = max(res, col-firstCol+1)
            q = q1   
        return res    