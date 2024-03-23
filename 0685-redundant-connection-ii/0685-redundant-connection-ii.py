class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.rank = Counter()

    def find(self,x):
        if not x in self.parent: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x==y: return False
        if self.rank[x]<self.rank[y]: self.parent[x] = y
        elif self.rank[x]>self.rank[x]: self.parent[y] = x
        else:
            self.parent[x] = y
            self.rank[y] += 1
        return True

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = max(max(a,b) for a,b in edges)
        
        parent = dict()
        A = []
        for i,(a,b) in enumerate(edges):
            if b not in parent:
                parent[b] = i
            else:
                A = [parent[b],i] # A is the indices of edges that leads to a indegree of 2
                break
        if not A:
            uf = UnionFind()
            j = None
            for i,(a,b) in enumerate(edges):
                if not uf.union(a,b): j = i
            return edges[j]
        else:
            uf = UnionFind()
            for i,(a,b) in enumerate(edges):
                if i==A[1]: continue
                if not uf.union(a,b): return edges[A[0]]
            return edges[A[1]]