class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        prefix = [0]
        cur = 0
        res = 0
        for num in nums:
            cur += num
            i = bisect.bisect(prefix,cur-goal-1)
            j = bisect.bisect(prefix, cur-goal)
            res += j-i
            prefix.append(cur)
        return res