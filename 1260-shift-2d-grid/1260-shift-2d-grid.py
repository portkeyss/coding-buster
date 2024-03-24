class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        A = [[0]*n for _ in range(m)]
        for j in range(n):
            for i in range(m):
                A[i][(j+k)%n] = grid[i][j]
        B = [[0]*n for _ in range(m)]
        for j in range(n):
            for i in range(m):
                if j<k%n:
                    B[(i+k//n+1)%m][j] = A[i][j]
                else:
                    B[(i+k//n)%m][j] = A[i][j]
        return B