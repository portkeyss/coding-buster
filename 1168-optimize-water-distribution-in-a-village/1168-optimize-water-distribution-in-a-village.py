class UnionFind:
    def __init__(self,m):
        self.rank = [0]*(m+1)
        self.parent = [-1]*(m+1)
    
    def find(self,x):
        if self.parent[x]==-1: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x==y: return False
        if self.rank[x]<self.rank[y]: self.parent[x]=y
        elif self.rank[x]>self.rank[y]: self.parent[y]=x
        else:
            self.parent[y] = x
            self.rank[x] += 1
        return True

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int: 
        edges = []
        for i,x in enumerate(wells):
            edges.append((x,0,i+1))
        for a,b,c in pipes:
            edges.append((c,a,b))
            edges.append((c,b,a))
        
        edges.sort()
        res = 0
        uf = UnionFind(n)
        for c,a,b in edges:
            if uf.union(a,b): res += c
        return res