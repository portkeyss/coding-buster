class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = [-500] + days #pad days to make indices start from 1
        n = len(days)
        dp = [0]+[float('inf')]*(n-1)
        for i in range(1,n):
            dp[i] = min(dp[i], dp[i-1]+costs[0])
            p = bisect.bisect_right(days,days[i]-7)
            dp[i] = min(dp[i], dp[p-1]+costs[1])
            p = bisect.bisect_right(days,days[i]-30)
            dp[i] = min(dp[i], dp[p-1]+costs[2])
        return dp[n-1]