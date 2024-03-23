class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9+7
        dp = defaultdict(lambda:0)#(cur,absenceCount,consecutiveLate)
        for _ in range(n):
            t = defaultdict(lambda:0)
            t[("A",1, 0)] = max(1,(dp[("L",0,1)]+dp[("L",0,2)]+dp[("P",0,0)])%mod)
            t[("L",1, 2)] = dp[("L",1, 1)]
            t[("L",1, 1)] = (dp[("A",1, 0)]+dp[("P",1, 0)])%mod
            t[("L",0, 2)] = dp[("L",0,1)]
            t[("L",0, 1)] = max(1,dp[("P",0, 0)])
            t[("P",1, 0)] = (dp[("A",1, 0)]+dp[("L",1, 2)]+dp[("L",1, 1)]+dp[("P",1, 0)])%mod
            t[("P",0, 0)] = max(1,(dp[("L",0, 2)]+dp[("L",0, 1)]+dp[("P",0, 0)])%mod)
            dp = t
        return sum(dp.values())%mod