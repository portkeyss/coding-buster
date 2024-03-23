class Solution:
    def racecar(self, target: int) -> int:
        @lru_cache(None)
        def f(d):
            b = d.bit_length()
            if (1<<b)-1==d:
                return b
            res = 1+b+f((1<<b)-1-d)
            for p in range(b-1):
                res = min(res, 1+b+p+f(d-((1<<(b-1))-1)+((1<<p)-1)))
            return res
        return f(target)