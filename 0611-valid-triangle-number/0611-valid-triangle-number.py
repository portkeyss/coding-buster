class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(n-2):
            k = i+2
            for j in range(i+1, n-1):
                k = max(k, j+1)
                while k < n and nums[k] < nums[i]+nums[j]:
                    k += 1
                ans += k - 1 - j              
        return ans