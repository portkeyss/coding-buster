class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            t = grid[i][j]
            grid[i][j] = 0
            ans = 0
            for d in directions:
                r, c = i+d[0], j+d[1]
                ans = max(ans, t+dfs(r,c))
            grid[i][j] = t
            return ans
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j))
        return res       