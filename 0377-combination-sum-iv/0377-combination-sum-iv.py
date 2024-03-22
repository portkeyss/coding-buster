class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @lru_cache(None)
        def f(t):
            if t==0: return 1
            if t<0: return 0
            ans = 0
            for x in nums:
                ans += f(t-x)
            return ans
        return f(target)