class Solution:
    def numWays(self, n: int, k: int) -> int:
        diffFromPrev = [0]*n
        sameAsPrev = [0]*n
        diffFromPrev[0] = k
        for i in range(1, n):
            diffFromPrev[i] = (k-1)*(diffFromPrev[i-1]+sameAsPrev[i-1])
            sameAsPrev[i] = diffFromPrev[i-1]
        return diffFromPrev[n-1]+sameAsPrev[n-1]