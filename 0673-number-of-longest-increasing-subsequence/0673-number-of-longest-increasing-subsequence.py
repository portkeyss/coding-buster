class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1,1] for _ in range(n)]
        A = [0]*(n+1)
        for j in range(n):
            for i in range(j):
                if nums[i] >= nums[j]: continue
                if dp[j][0] > 1+dp[i][0]: continue
                elif dp[j][0] == 1+dp[i][0]:
                    dp[j][1] += dp[i][1]
                else:
                    dp[j][0] = 1+dp[i][0]
                    dp[j][1] = dp[i][1]
            A[dp[j][0]] += dp[j][1]
        k = n
        while k>=0 and A[k]==0:
            k -= 1
        return A[k]