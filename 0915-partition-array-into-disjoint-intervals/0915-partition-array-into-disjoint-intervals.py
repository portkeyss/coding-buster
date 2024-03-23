class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        leftMax = [None]*len(nums)
        leftMax[0] = nums[0]
        for i in range(1,len(nums)):
            leftMax[i]=max(leftMax[i-1], nums[i])
        
        res = None
        rightMin = math.inf
        i = len(nums)-1
        while i > 0:
            rightMin = min(rightMin,nums[i])
            if rightMin >= leftMax[i-1]:
                res = i
            i -= 1
        return res
        