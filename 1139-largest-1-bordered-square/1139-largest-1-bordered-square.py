class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        A = [[-1]*n for _ in range(m)]
        B = [[-1]*n for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if grid[i][j] == 1:
                    if j==n-1 or A[i][j+1] == -1: A[i][j] = j
                    else: A[i][j] = A[i][j+1]
                    if i==m-1 or B[i+1][j] == -1: B[i][j] = i
                    else: B[i][j] = B[i+1][j]
        edge = 0
        for i in range(m):
            for j in range(n):
                for a in range(min(m-i,n-j),edge,-1):
                    k = i+a-1
                    l = j+a-1
                    if A[i][j]>=l and B[i][j]>=k and A[k][j]>=l and B[i][l]>=k:
                        edge = a
                        break
        return edge*edge