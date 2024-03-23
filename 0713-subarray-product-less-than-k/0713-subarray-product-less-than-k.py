class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < 2: return 0
        i = 0
        j = 0
        prod = 1
        res = 0
        while j < len(nums):
            prod *= nums[j]
            while i <= j and prod >= k:
                prod /= nums[i]
                i += 1
            res += j-i+1
            j += 1
        return res