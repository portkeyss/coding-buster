class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        @lru_cache(None)
        def f(i,j):
            if i+1==j: return 0
            res = inf
            for k in range(i+1,j):
                res = min(res, f(i,k)+values[i]*values[k]*values[j]+f(k,j))
            return res

        return f(0,n-1)