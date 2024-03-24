class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = defaultdict(lambda:0)
        def g(t,n):
            if t < n or t > n*f:
                return 0
            if n == 1:
                return 1
            if (t,n) not in dp:
                for i in range(1,f+1):
                    dp[(t,n)] += g(t-i,n-1)
            return dp[(t,n)]
        return g(target,d) % (10**9+7)