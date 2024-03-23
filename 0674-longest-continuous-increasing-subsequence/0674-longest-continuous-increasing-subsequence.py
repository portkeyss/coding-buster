class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        ans = 1
        curLen = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curLen += 1
                ans = max(ans, curLen)
            else:
                curLen = 1
        return ans