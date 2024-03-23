class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = defaultdict(lambda:0)
        for n in nums:
            freq[n] += 1
        degree = max(freq.values())
        status = {}
        res = len(nums)
        for i,n in enumerate(nums):
            if freq[n] == degree:
                if n not in status:
                    status[n] = [i, 1]  
                else:
                    status[n][1] += 1
                if status[n][1] == degree:
                    res = min(res, i-status[n][0]+1)
        return res        