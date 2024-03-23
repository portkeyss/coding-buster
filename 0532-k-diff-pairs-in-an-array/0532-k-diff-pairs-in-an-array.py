class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = defaultdict(int)
        res = 0
        for num in nums:
            if num in count and (k > 0 or count[num] > 1):
                continue
            if num - k in count:
                res += 1
            count[num] += 1
        return res