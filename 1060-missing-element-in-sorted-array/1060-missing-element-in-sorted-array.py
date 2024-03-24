class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(1,len(nums)):
            if nums[i] > nums[0] + k + i - 1:
                return nums[0] + k + i - 1
        return nums[0] + k + len(nums) - 1
        