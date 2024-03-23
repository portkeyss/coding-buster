class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        sm = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if 2 * left_sum == sm - num: # left_sum + num + right_sum = sum -> 2 * left_sum = sum - num
                return i
            left_sum += num
        return -1