class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = [] #monotonic decreasing stack
        n = len(nums)
        for i in range(n):
            if not stack or nums[stack[-1]]>nums[i]:
                stack.append(i)
        res = 0
        for j in range(n-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[j]:
                res = max(res, j-stack.pop())
        return res