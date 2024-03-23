class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if k==0: return 1
        if k>n*(n-1)//2: return 0
        mod = 10**9+7
        dp = [1]+[0]*k
        for i in range(1,n+1):
            t = [1]+[0]*k
            for j in range(1,min(i*(i-1)//2,k)+1):
                t[j] = (t[j-1]+dp[j])%mod
                if j-i>=0: t[j] = (t[j]-dp[j-i])%mod
            dp = t
        return dp[k]