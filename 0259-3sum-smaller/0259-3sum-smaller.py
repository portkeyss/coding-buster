class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()    
        def twoSumSmaller(nums, start, end, t):
            left, right = start, end
            cnt = 0
            while left < right:
                if nums[left] + nums[right] < t:
                    cnt += right - left
                    left += 1
                else:
                    right -= 1
            return cnt
        res = 0
        for i in range(len(nums)):
            res += twoSumSmaller(nums, i+1, len(nums)-1, target-nums[i])
        return res