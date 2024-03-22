class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l<=r:
            m = (l+r)//2
            if m==0 or nums[m-1]<nums[m]:
                if m==n-1 or nums[m]>nums[m+1]:
                    return m
                else:
                    l = m+1
            else:
                r = m-1