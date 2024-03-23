class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        mx = -10**15
        mx = max(nums[-3]*nums[-2]*nums[-1], nums[0]*nums[1]*nums[-1])
        return mx
        