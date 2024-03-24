class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        dp = [1]*n
        for j in range(n):
            for i in range(j):
                if all(strs[k][i]<=strs[k][j] for k in range(m)):
                    dp[j] = max(dp[j],dp[i]+1)
        return n-max(dp)