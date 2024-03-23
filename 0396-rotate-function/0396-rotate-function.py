class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        #it can be mathematically deduced that F(k) = F(k-1) + sum(nums) + n*nums[n-k]
        F = sum(i*num for i,num in enumerate(nums))
        sm = sum(nums)
        res = F
        n = len(nums)
        for i in range(1,n):
            F += sm-n*nums[n-i]
            res = max(res, F)
        return res