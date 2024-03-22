class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        #brute force O((mn)**2) time complexity
        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def bfs(sx,sy):
            q = deque()
            q.append([sx,sy])
            dist = [[float('inf')]*n for _ in range(m)]
            dist[sx][sy] = 0
            while q:
                x0,y0 = q.popleft()
                for d in directions:
                    x, y = x0+d[0], y0+d[1]
                    if x<0 or x>=m or y<0 or y>=n or grid[x][y] != 0 or dist[x][y] < float('inf'):
                        continue
                    dist[x][y] = dist[x0][y0] + 1
                    q.append([x,y]) 
                    totDist[x][y] += dist[x][y]
                    reachable[x][y] += 1
                    
        reachable = [[0]*n for _ in range(m)]
        totDist =  [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                bfs(i,j)
        
        buildingNum = sum(a == 1 for l in grid for a in l)
        res = float('inf')
        for i in range(m):
            for j in range(n):
                if reachable[i][j] == buildingNum:
                    res = min(res, totDist[i][j])
        return res if res < float('inf') else -1