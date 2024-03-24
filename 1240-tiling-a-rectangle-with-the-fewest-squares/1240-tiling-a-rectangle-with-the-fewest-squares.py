class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n==m: return 1
        if n>m: return self.tilingRectangle(m,n)
        self.res = inf
        self.cache = dict()
        def f(skyline, cnt):
            if cnt>=self.res: return
            if skyline==tuple([n]*m): 
                self.res =  min(self.res, cnt)
            if skyline in self.cache and self.cache[skyline]<=cnt: return
            self.cache[skyline]=cnt
            pos = -1
            minH = inf
            for i in range(m):
                if skyline[i]<minH:
                    pos = i
                    minH = skyline[i]
            j = pos
            while j<m and skyline[j]==minH and j-pos+1<=n-minH:
                j += 1
            for k in range(j-1,pos-1,-1):
                newSkyline = [x for x in skyline]
                for l in range(pos,k+1):
                    newSkyline[l] += k-pos+1
                f(tuple(newSkyline), cnt+1)
                
        f(tuple([0]*m), 0)
        return self.res