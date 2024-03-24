class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        s = -1
        for i in range(len(nums)):
            j = bisect.bisect(nums, k -1 - nums[i])
            if i >= j-1:
                break
            s = max(nums[i]+nums[j-1], s)
        return s