class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        area = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    area += grid[i][j] * 4 + 2
                if i >= 1:
                    area -= 2 * min(grid[i-1][j], grid[i][j])
                if j >= 1:
                    area -= 2 * min(grid[i][j-1], grid[i][j])                   
        return area