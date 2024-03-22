class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missing = 1
        res = 0
        i = 0
        while missing<=n:
            if i<len(nums) and nums[i]<=missing:
                missing += nums[i]
                i += 1
            else:
                missing += missing
                res += 1
        return res