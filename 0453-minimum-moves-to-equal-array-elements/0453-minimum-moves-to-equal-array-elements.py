class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Only the relative positions betwen numbers matters, (n-1) numbers increment is equivalent to 1 number decrement
        if not nums:
            return 0
        min_num = min(nums)
        return sum([num - min_num for num in nums])
        