class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        A = sorted(zip(startTime, endTime, profit), key = lambda x: x[1])
        dp = [[0,0]] #the first element is the end time, the second is the maxprofit up until this end time
        for start, end, p in A:
            j = bisect.bisect(dp, [start+1]) - 1
            if dp[j][-1] + p > dp[-1][-1]:
                dp.append([end, dp[j][-1]+p])
        return dp[-1][-1]