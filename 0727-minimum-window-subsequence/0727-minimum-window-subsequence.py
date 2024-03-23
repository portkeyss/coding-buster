class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [[-1]*n for _ in range(m)]
        res = (10**5, 10**6) #starting point and end point
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    if j == 0: dp[i][j] = i
                    else:
                         if i>0 and j>0: dp[i][j] = dp[i-1][j-1]
                    if j == n-1 and dp[i][j] != -1 and (i-dp[i][j] < res[1]-res[0] or  i-dp[i][j] == res[1]-res[0] and i < res[0]):
                        res = [dp[i][j],i]
                else:
                    if i > 0: dp[i][j] = dp[i-1][j]
        return s1[res[0]:res[1]+1] if res[0] < m else ""              