class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = m*(1<<(n-1))
        for j in range(1,n):
            ones = 0
            for i in range(m):
                if grid[i][j]==grid[i][0]:
                    ones += 1
            res += max(ones, m-ones)*(1<<(n-1-j))
        return res