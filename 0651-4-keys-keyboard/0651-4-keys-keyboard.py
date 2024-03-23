class Solution:
    def maxA(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(n+1):
            dp[i] = i
            for j in range(i-2):
                dp[i] = max(dp[i], dp[j]*(i-j-1))
        return dp[n]