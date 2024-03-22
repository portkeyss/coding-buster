class NumArray:

    def __init__(self, nums: List[int]):
        self.cumSum = [0]
        for n in nums:
            self.cumSum.append(n + self.cumSum[-1])

    def sumRange(self, i: int, j: int) -> int:
        return self.cumSum[j+1] - self.cumSum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)