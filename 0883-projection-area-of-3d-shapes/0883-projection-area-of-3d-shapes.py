class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        x = 0
        for i in range(n):
            x += max(grid[i])
        for j in range(n):
            x += max(grid[i][j] for i in range(n))
        x += sum(grid[i][j]>0 for i in range(n) for j in range(n))
        return x