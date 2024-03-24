class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        class UnionFind:
            def __init__(self, m):
                self.m = m
                self.size = [1]*m
                self.parent = [-1]*m
            
            def find(self,a):
                if self.parent[a]==-1: return a
                self.parent[a] = self.find(self.parent[a])
                return self.parent[a]
            
            def union(self,a,b):
                p, q = self.find(a), self.find(b)
                if p==q: return False
                elif self.size[p]>self.size[q]:
                    self.parent[q] = p
                    self.size[p] += self.size[q]
                else:
                    self.parent[p] = q
                    self.size[q] += self.size[p]
                return self.size[p]==self.m or self.size[q]==self.m
                
        logs.sort(key=lambda v:v[0])
        uf = UnionFind(n)
        for t,x,y in logs:
            if uf.union(x,y): return t
        return -1