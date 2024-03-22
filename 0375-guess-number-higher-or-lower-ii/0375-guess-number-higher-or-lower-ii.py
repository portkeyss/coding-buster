class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def f(i,j):
            if i>=j: return 0
            ans = inf
            for k in range(i,j+1):
                ans = min(ans, k+max(f(i,k-1),f(k+1,j)))
            return ans
        return f(1,n)