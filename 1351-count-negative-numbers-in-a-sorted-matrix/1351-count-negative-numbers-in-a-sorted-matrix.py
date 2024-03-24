class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        j = 0
        res = 0
        for i in range(m-1,-1,-1):
            while j < n and grid[i][j] >= 0: j += 1
            res += n-j
        return res