class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        mid = (n-1)//2
        return sum(abs(nums[mid]-num) for num in nums)