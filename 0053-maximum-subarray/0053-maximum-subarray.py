class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = nums[0]
        lgst_sum_including_cur_idx = 0
        for i in range(len(nums)):
            lgst_sum_including_cur_idx = max(lgst_sum_including_cur_idx + nums[i], nums[i])
            largest = max(largest, lgst_sum_including_cur_idx)
        return largest