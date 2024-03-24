class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sm = 0
        for i,num in enumerate(nums):
            if num%2==0:
                sm+=num
        res = []
        for v,i in queries:
            if nums[i]%2==0:
                if v%2==0:
                    sm += v
                else:
                    sm -= nums[i]
            else:
                if v%2==1:
                    sm += nums[i]+v
            res.append(sm)
            nums[i] += v
        return res