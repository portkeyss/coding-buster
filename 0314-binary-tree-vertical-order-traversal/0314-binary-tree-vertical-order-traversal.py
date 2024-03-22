# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """  
        self.hp = []
        self.idx = 0
        self.traverse(root, 0, 0)
        prev_x = - 1000000 # any arbitary integer less than anything index of the tree
        res = []
        while self.hp:
            x, _, _, val = heapq.heappop(self.hp)
            if x == prev_x:
                res[-1].append(val)
            else:
                res.append([val])
            prev_x = x
        return res
            
        
    def traverse(self, root, x, y): # use index in enforcing order
        if not root:
            return
        #we traverse from left tree to root to right tree to ensure correct ordering
        self.traverse(root.left, x-1, y-1) 
        heapq.heappush(self.hp, (x, -y, self.idx, root.val))
        self.idx += 1
        self.traverse(root.right, x+1, y-1)
        
        