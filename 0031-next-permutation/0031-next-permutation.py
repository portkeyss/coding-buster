class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p = n - 2
        while p >= 0 and nums[p] >= nums[p+1]:
            p -= 1
        if p >= 0:
            q = n - 1
            while nums[q] <= nums[p]:
                q -= 1
            nums[p], nums[q] = nums[q], nums[p]
        l, r = p+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1