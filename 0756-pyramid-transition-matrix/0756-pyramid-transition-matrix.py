class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        B = defaultdict(list)
        for p in allowed:
            B[p[:2]].append(p[2])
        
        @lru_cache(None)
        def f(ground): 
            if len(ground)==1: return True
            l = [""]
            for i in range(len(ground)-1):
                temp = []
                for a in B[ground[i:i+2]]:
                    for x in l:
                        temp.append(x+a)
                l = temp
                if l==[]: return False
            return any(f(x) for x in l)
            
        return f(bottom)