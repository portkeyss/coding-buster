class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        bucket = [0]*100001
        for n in nums:
            bucket[n+50000] += 1
        res = []
        for i in range(100001):
            while bucket[i]:
                res.append(i-50000)
                bucket[i] -= 1
        return res