class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = 0
        #compress out all non positive numbers
        for i in range(len(nums)):
            if nums[i]>0:
                nums[n] = nums[i]
                n += 1
              
        for i in range(n):
            if abs(nums[i])<=n:
                j = abs(nums[i])-1
                nums[j] = -abs(nums[j])
        for i in range(n):
            if nums[i]>0: return i+1
        return n+1