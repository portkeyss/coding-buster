# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        self.hq = [] # heap queue in the order of positive x-coordinate, negative y-coorindate, and in value of nodes if the coordinates are the same
        self.traversal(root, 0, 0)
        res = []
        prev_x = -10000 # define an initially out of bound previous coordinates
        while self.hq:
            x, _, val = heapq.heappop(self.hq)           
            if x == prev_x:
                res[-1].append(val)
            else:
                res.append([val])
            prev_x= x      
        return res
    
    def traversal(self, root, x, y):
        if not root:
            return
        heapq.heappush(self.hq, (x, -y, root.val))
        self.traversal(root.left, x-1, y-1)
        self.traversal(root.right, x+1, y-1)
        