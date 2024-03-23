class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(1001))
        rank = [0]*1001
        def find(a):
            if parent[a]==a: return a
            parent[a] = find(parent[a])
            return parent[a]
        
        def union(a,b):
            ap, bp = find(a), find(b)
            if ap == bp: return False
            if rank[ap] > rank[bp]:
                parent[bp] = ap
            elif rank[a] < rank[bp]:
                parent[ap] = bp
            else:
                parent[bp] = ap
                rank[ap] += 1
            return True
        
        for x,y in edges:
            if union(x,y) is False: return [x,y]