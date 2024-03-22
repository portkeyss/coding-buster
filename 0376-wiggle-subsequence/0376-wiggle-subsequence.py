class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        valley = peak = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i-1]<nums[i]:
                peak = valley+1
            elif nums[i-1]>nums[i]:
                valley = peak+1
        return max(peak, valley)