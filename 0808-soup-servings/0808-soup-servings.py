class Solution:
    def soupServings(self, n: int) -> float:
        @lru_cache(None)
        def f(a,b):
            if a<=0 and b>0: return 1
            if a<=0 and b<=0: return 0.5
            if a>0 and b<=0: return 0
            return (f(a-100,b)+f(a-75,b-25)+f(a-50,b-50)+f(a-25,b-75))*0.25
        
        if n>10000: return 1
        return f(n,n)