class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        idx = -1
        area = dict()
        def dfs(i,j):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] < 1:
                return 0
            a = 1
            grid[i][j] = idx
            for d in directions:
                a += dfs(i+d[0], j+d[1])
            return a
        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[idx] = dfs(i,j)
                    ans = max(ans, area[idx])
                    idx -= 1
        if ans == 0:
            return 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbors = set()
                    for d in directions:
                        x, y = i+d[0], j+d[1]
                        if 0 <= x < n and 0 <= y < n and grid[x][y] in area:
                            neighbors.add(grid[x][y])
                    a = 1 + sum(area[k] for k in neighbors)
                    ans = max(ans, a)
        return ans       