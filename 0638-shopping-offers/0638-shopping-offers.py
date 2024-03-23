class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        special=list(filter(lambda s:all(s[i]<=needs[i] for i in range(n)),special))
        
        @lru_cache(None)
        def f(x):
            v = sum(x[i]*price[i] for i in range(n))
            for s in special:
                tmp = [x[i]-s[i] for i in range(n)]
                if min(tmp) >= 0:
                    v = min(v, f(tuple(tmp))+s[n])
            return v
                     
        return f(tuple(needs))