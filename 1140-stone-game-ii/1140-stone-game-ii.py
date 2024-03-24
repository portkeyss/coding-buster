class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        @lru_cache(None)
        def f(k,M,A):#A==True means Alice's turn
            if k==n: return 0
            if A:
                a = 0
                s = 0
                for x in range(1,min(2*M,n-k)+1):
                    s += piles[k+x-1]
                    a = max(a, s+f(k+x,max(M,x),1-A))
            else:
                a = math.inf
                for x in range(1,min(2*M,n-k)+1):
                    a = min(a, f(k+x,max(M,x),1-A))
            return a
        
        return f(0,1,True)