class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        x = nums[0]
        if x==1: return True
        for i in range(1,len(nums)):
            x = gcd(x,nums[i])
            if x==1: return True
        return False