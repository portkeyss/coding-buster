class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        mod = 10**9+7
        rank = [0]*m
        parent = [-1]*m
        def find(x):
            if parent[x]==-1: return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            px = find(x)
            py = find(y)
            if px==py: return
            if rank[px]<rank[py]:
                parent[px] = py
            elif rank[px]>rank[py]:
                parent[py] = px
            else:
                parent[px] = py
                rank[py] += 1
        
        for i in range(m-1):
            for j in range(i+1,m):
                diff = 0
                for k in range(n):
                    if strs[i][k]!=strs[j][k]:
                        diff+=1
                        if diff>2: break
                if diff<=2: union(i,j)
                
        return len(set(find(i) for i in range(m)))