class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        for s in strs:
            ctr = Counter(s)
            a, b = ctr["0"], ctr["1"]
            for i in range(m+1):
                for j in range(n+1):
                    dp[i][j] = dp[i][j]
            for i in range(m, a-1, -1):
                for j in range(n, b-1, -1):
                    dp[i][j] = max(dp[i][j], 1+dp[i-a][j-b])
        return dp[m][n]