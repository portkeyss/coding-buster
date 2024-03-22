class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        A = [[0]*n for _ in range(m)]
        res = 0
        for i in range(m):
            leftEnemies = 0
            for j in range(n):
                if grid[i][j] == 'W':
                    leftEnemies = 0
                if grid[i][j] == 'E':
                    leftEnemies += 1
                else:
                    A[i][j] = leftEnemies
            rightEnemies = 0
            for j in range(n-1,-1,-1):
                if grid[i][j] == 'W':
                    rightEnemies = 0
                if grid[i][j] == 'E':
                    rightEnemies += 1
                else:
                    A[i][j] += rightEnemies
        for j in range(n):
            upperEnemies = 0
            for i in range(m):
                if grid[i][j] == 'W':
                    upperEnemies = 0
                if grid[i][j] == 'E':
                    upperEnemies += 1
                else:
                    A[i][j] += upperEnemies
            lowerEnemies = 0
            for i in range(m-1,-1,-1):
                if grid[i][j] == 'W':
                    lowerEnemies = 0
                if grid[i][j] == 'E':
                    lowerEnemies += 1
                else:
                    A[i][j] += lowerEnemies
                    res = max(res, A[i][j])
        return res  