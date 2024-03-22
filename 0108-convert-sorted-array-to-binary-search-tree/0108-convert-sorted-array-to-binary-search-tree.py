# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """        
        return self.split(nums, 0, len(nums) - 1)
    
    def split(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end)/2
        root = TreeNode(nums[mid])
        left = self.split(nums, start, mid - 1)
        right = self.split(nums, mid + 1, end)
        root.left = left
        root.right = right
        return root
        