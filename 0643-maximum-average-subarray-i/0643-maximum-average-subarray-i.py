class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sm = sum(nums[:k])
        res = sm/k
        for i in range(k,len(nums)):
            sm = sm+nums[i]-nums[i-k]
            res = max(res, sm/k)
        return res    