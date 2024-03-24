class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)
        for j in range(n):
            p = 0
            for i in range(j,max(-1,j-k),-1):
                p = max(p, arr[i])
                dp[j+1] = max(dp[j+1], dp[i]+p*(j-i+1))
        return dp[n]