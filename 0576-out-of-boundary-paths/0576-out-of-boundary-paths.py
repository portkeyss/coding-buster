class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        A = [[0]*n for _ in range(m)]
        A[startRow][startColumn]=1
        res = 0
        for move in range(maxMove):
            B = [[0]*n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    if A[r][c] == 0: continue
                    for dx,dy in directions:
                        r1 = r+dx
                        c1 = c+dy
                        if 0<=r1<m and 0<=c1<n:
                            B[r1][c1] += A[r][c]
                        else:
                            res += A[r][c]
            A = B
        return res%(10**9+7)