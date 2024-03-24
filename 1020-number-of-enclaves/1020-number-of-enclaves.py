class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        land = sum(grid[i][j] for i in range(m) for j in range(n))
        s = set()
        for i in range(m):
            if grid[i][0]==1: s.add((i,0))
            if grid[i][n-1]==1: s.add((i,n-1))
        for j in range(n):
            if grid[0][j]==1: s.add((0,j))
            if grid[m-1][j]==1: s.add((m-1,j))
        q = deque(s)
        ds = [[1,0],[0,1],[-1,0],[0,-1]]
        while q:
            x,y = q.popleft()
            for dx,dy in ds:
                if 0<=x+dx<m and 0<=y+dy<n and (x+dx,y+dy) not in s and grid[x+dx][y+dy]==1:
                    q.append((x+dx,y+dy))
                    s.add((x+dx,y+dy))
        return land-len(s)