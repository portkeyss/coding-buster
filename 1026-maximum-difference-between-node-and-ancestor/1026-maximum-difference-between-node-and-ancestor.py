# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.maxDiff(root, 0, root.val, root.val) # 0 is the initial maxDiff value; To keep our recursion formalism consistent from the root, we need to make sure the root has zero distance from its 'virtual' ancestors, therefore maxAncestorVal and minAncestorVal should be set equal to root value
    
    def maxDiff(self, root, maxDist, maxAncestorVal, minAncestorVal):
        maxDist = max(maxDist, abs(root.val - maxAncestorVal), abs(root.val - minAncestorVal))
        maxAncestorVal = max(root.val, maxAncestorVal)
        minAncestorVal = min(root.val, minAncestorVal)
        if root.left:
            maxDist = self.maxDiff(root.left, maxDist, maxAncestorVal, minAncestorVal)
        if root.right:
            maxDist = self.maxDiff(root.right, maxDist, maxAncestorVal, minAncestorVal)
        return maxDist
        
        
        