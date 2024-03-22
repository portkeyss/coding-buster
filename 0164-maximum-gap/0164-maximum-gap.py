class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        mi, mx, n = min(nums), max(nums), len(nums)
        if mi == mx or n < 2: return 0
        bucketSize = ceil((mx-mi)/(n-1))
        bucket = [[math.inf, -math.inf] for _ in range(n)]
        for a in nums:
            k = (a - mi)//bucketSize
            bucket[k][0] = min(bucket[k][0], a)
            bucket[k][1] = max(bucket[k][1], a)
        diff = 0
        prevMax = bucket[0][1]
        for k in range(1,n):
            if bucket[k][0] < math.inf:
                diff = max(diff, bucket[k][0] - prevMax)
                prevMax = bucket[k][1]
        return diff