class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        i = bisect.bisect_left(nums, target)
        j = bisect.bisect(nums, target)
        return j - i > len(nums)//2