class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        A = [max(grid[i]) for i in range(n)]
        B = [max(grid[i][j] for i in range(n)) for j in range(n)]
        res = 0
        for i in range(n):
            for j in range(n):
                res += min(A[i], B[j])-grid[i][j]
        return res