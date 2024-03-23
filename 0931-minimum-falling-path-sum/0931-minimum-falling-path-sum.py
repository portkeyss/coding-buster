class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = matrix[0].copy()
        for i in range(1,m):
            t = [inf]*n
            for j in range(n):
                t[j] = dp[j]+matrix[i][j]
                if j-1>=0: t[j] = min(t[j],dp[j-1]+matrix[i][j])
                if j+1<n: t[j] = min(t[j],dp[j+1]+matrix[i][j])
            dp = t
        return min(dp)