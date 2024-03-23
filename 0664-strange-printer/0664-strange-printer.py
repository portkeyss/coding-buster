class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def f(start,end):
            if s[start:end+1]==s[end]*(end+1-start):return 0
            ans = inf
            for i in range(start,end):
                x = f(start,i)+f(i+1,end)
                if s[i]!=s[end]: x += 1
                ans = min(ans,x)
            return ans

        return 1+f(0,n-1)