class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        rank = defaultdict(lambda:0)
        parent = defaultdict(lambda:-1)
        
        def find(x):
            if parent[x]==-1: return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            a = find(x)
            b = find(y)
            if a==b: return False
            if rank[a]<rank[b]:
                parent[a] = b
            elif rank[a]>rank[b]:
                parent[b] = a
            else:
                parent[a] = b
                rank[b] += 1
            return True
        
        islands = []
        count = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        for r,c in positions:
            if (r,c) not in parent:
                newIsland = True
                count += 1
                parent[(r,c)] = -1
                for dr,dc in directions:
                    if 0<=r+dr<m and 0<=c+dc<n:
                        if (r+dr,c+dc) in parent:
                            if union((r,c),(r+dr,c+dc)): count-=1
            islands.append(count)
        return islands