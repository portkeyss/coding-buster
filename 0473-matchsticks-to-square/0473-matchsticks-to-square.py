class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        totLength = sum(matchsticks)
        if totLength%4: return False
        edge = totLength//4
        matchsticks.sort(reverse=True)#This line is not strictly necessary
        
        @lru_cache(None)
        def f(i,lengths):
            if i==n: return True
            for j in range(4):
                if lengths[j]+matchsticks[i]>edge: continue
                ls = list(lengths)
                ls[j] += matchsticks[i]
                ls.sort()  
                if f(i+1,tuple(ls)): return True
            return False
        return f(0,(0,0,0,0))