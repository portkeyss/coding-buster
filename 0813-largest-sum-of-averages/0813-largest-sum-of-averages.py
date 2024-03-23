class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        dp = [prefix[i]/i for i in range(1,n+1)]
        for _ in range(2,k+1):
            for i in range(n-1,-1,-1):#the reason for reverse iteration is that the updated value will not be used in later iteration steps; if we do natural order iteration, we may need to construct a new dp in each step
                for j in range(i):
                    dp[i] = max(dp[i], dp[j]+(prefix[i+1]-prefix[j+1])/(i-j))
        return dp[n-1]