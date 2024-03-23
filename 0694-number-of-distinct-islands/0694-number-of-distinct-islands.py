class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        islands = set()
        def dfs(i,j, i0, j0):
            positions.append((i-i0, j-j0))
            seen.add((i,j))
            for d in directions:
                x, y = d[0] + i, d[1] + j
                if x < 0 or x >= m or y < 0 or y >= n or (x, y) in seen or grid[x][y] == 0:
                    continue
                dfs(x,y,i0,j0)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or (i,j) in seen:
                    continue
                positions = []
                dfs(i,j, i,j)              
                islands.add(frozenset(positions))
        return len(islands)