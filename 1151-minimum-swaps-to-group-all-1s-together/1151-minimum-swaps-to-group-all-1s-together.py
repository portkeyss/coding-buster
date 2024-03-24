class Solution:
    def minSwaps(self, data: List[int]) -> int:
        m = sum(data)
        n = len(data)
        p = sum(data[:m])
        maxSumInWindow = p
        for i in range(m, n):
            p = p - data[i-m] + data[i]
            maxSumInWindow = max(maxSumInWindow, p)
        return m - maxSumInWindow