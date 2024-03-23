class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        sum1 = sum(nums)
        sum2 = sum(set(nums))
        dup = sum1-sum2
        n = len(nums)
        missing = (1+n)*n//2-sum2
        return [dup, missing]