class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = [[1,0],[0,1],[-1,0],[0,-1]]
        s1, s2 = None, None
        self.count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    s1, s2 = i,j
                elif grid[i][j]==0:
                    self.count += 1
        
        def dfs(x,y):
            res = 0
            for dx,dy in d:
                x1 = x+dx
                y1 = y+dy
                if 0<=x1<m and 0<=y1<n and grid[x1][y1] in [0,2]:
                    if grid[x1][y1]==0:
                        grid[x1][y1]=-1
                        self.count -= 1
                        res += dfs(x1,y1)
                        grid[x1][y1]=0
                        self.count += 1
                    elif grid[x1][y1]==2:
                        res += 1 if self.count==0 else 0
            return res
                    
        return dfs(s1,s2)