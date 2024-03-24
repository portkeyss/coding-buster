class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        A = [0]*m
        B = [0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    A[i]+=1
                    B[j]+=1
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]>0 and A[i]+B[j]>2: res += 1
        return res