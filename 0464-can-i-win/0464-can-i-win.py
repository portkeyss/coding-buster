class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        m, d = maxChoosableInteger, desiredTotal
        if (m+1)*m//2 < d: return False #this line is important, it ensures that A's success means B's failure
        if d == 0: return True

        @lru_cache(None)
        def f(n, used):
            for i in range(1,m+1):
                if (1<<i)&used == 0:
                    if n-i <= 0 or f(n-i, (1<<i)+used) is False:
                        return True  
            return False
                
        return f(d, 0)