class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def normalize(l):
            rows, cols = zip(*l)
            minRow, minCol = min(rows), min(cols)
            return frozenset((r-minRow, c-minCol) for r,c in l)
        
        islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    grid[i][j]=0
                    island = []
                    q = deque()
                    q.append((i,j))
                    island.append((i,j))
                    while q:
                        r,c = q.popleft()
                        for dr,dc in directions:
                            r1,c1 = r+dr,c+dc
                            if 0<=r1<m and 0<=c1<n and grid[r1][c1]==1:
                                grid[r1][c1]=0
                                q.append((r1,c1))
                                island.append((r1,c1))
                    island = normalize(island)
                    if island in islands: continue
                    if normalize([(-c,r) for r,c in island]) in islands: continue
                    if normalize([(-r,-c) for r,c in island]) in islands: continue
                    if normalize([(c,-r) for r,c in island]) in islands: continue
                    if normalize([(r,-c) for r,c in island]) in islands: continue
                    if normalize([(-r,c) for r,c in island]) in islands: continue
                    if normalize([(c,r) for r,c in island]) in islands: continue
                    if normalize([(-c,-r) for r,c in island]) in islands: continue
                    islands.add(island)
        return len(islands)           