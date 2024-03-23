class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return True
        i = 0
        while i < n -1:
            if nums[i] <= nums[i+1]:
                i += 1
            else:
                break
        if i == n - 2:
            return True
       
        j = n - 2
        while j >= i:
             if nums[j] <= nums[j+1]:
                j -= 1
             else:
                break
        if j > i:
            return False
        else:
            return i+2 > n - 1 or nums[i] <= nums[i+2] or i-1 < 0 or nums[i-1] <= nums[i+1]