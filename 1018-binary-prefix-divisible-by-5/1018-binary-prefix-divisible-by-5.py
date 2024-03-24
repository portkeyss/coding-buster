class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        x = 0
        res = []
        for num in nums:
            x = x*2+num
            res.append(True if x%5==0 else False)
        return res