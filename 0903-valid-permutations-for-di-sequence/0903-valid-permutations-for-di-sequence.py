class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n = len(s)
        mod = 10**9+7
        dp = [1]+[0]*n
        for j,c in enumerate(s):
            t = [0]*(n+1)
            if c=="D":
                a = 0
                for i in reversed(range(j+2)):
                    a = (a+dp[i])%mod
                    t[i] = (t[i]+a)%mod
            else:
                b = 0
                for i in range(j+2):
                    t[i] = (t[i]+b)%mod
                    b = (b+dp[i])%mod
            dp = t
        res = 0
        for x in dp:
            res = (res+x)%mod
        return res