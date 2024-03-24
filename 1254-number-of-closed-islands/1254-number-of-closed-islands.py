class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n:
                return False
            if grid[r][c] != 0:
                return True
            grid[r][c] = -1
            ans = True
            for d in directions:
                x, y = r+d[0], c+d[1]
                if not dfs(x,y):
                    ans = False
            return ans
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += dfs(i,j)
        return res