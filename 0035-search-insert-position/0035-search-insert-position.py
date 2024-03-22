class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        if target <= nums[0]:
            return 0
        if target > nums[j]:
            return j + 1
        while i < j:
            mid = i + (j - i)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        return j