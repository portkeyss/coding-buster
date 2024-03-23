class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        res = []
        for num in nums:
            if num in s:
                res.append(num)
            else:
                s.add(num)
        return res