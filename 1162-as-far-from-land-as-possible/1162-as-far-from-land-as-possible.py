class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        drs = [[1,0],[0,1],[-1,0],[0,-1]]
        outer = []
        sm = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    outer.append([i,j])
                sm += grid[i][j]
        if sm in [0,n*n]: return -1
        
        step = 0
        while True:
            t = []
            while outer:
                i,j = outer.pop()
                for d0,d1 in drs:
                    x,y = i+d0, j+d1
                    if 0<=x<n and 0<=y<n and grid[x][y]==0:
                        t.append([x,y])
                        grid[x][y] = 1
            if len(t)==0: return step
            outer = t
            step += 1