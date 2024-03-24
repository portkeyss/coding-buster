class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        prefix = [0]
        x = 0
        for stone in stones:
            x += stone
            prefix.append(x)

        @lru_cache(None)
        def f(s,e,seg):
            if seg==1:
                if s==e: return 0
                if e-s+1==k: return prefix[e+1]-prefix[s]
                if e-s+1<k: return inf
                return prefix[e+1]-prefix[s]+f(s,e,k)
            else:
                if e-s+1<seg: return inf
                res = inf
                for i in range(s,e):
                    res = min(res, f(s,i,1)+f(i+1,e,seg-1))
                return res
            
        res = f(0,n-1,1)
        return res if res<inf else -1