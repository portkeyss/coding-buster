class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        def decrement(nums, idx, n):
            t1 = nums[idx-1] if idx-1 >= 0 else float('inf')
            t2 = nums[idx+1] if idx+1 < n else float('inf')
            t = min(t1, t2)
            return nums[idx]-t+1 if t <= nums[idx] else 0
        
        a = 0
        for i in range(1,len(nums),2):
            a += decrement(nums, i, n)
        b = 0
        for i in range(0,len(nums),2):
            b += decrement(nums, i, n)
        return min(a,b)