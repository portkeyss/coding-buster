class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        A = [0]*m
        B = [0]*n
        dist = [0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    A[i] += 1
                    B[j] += 1
                    dist[0] += i+j
                    
        tot = sum(A)
        res = dist[0]
        left = B[0]
        for j in range(1,n):
            dist[j] = dist[j-1]+(2*left-tot)
            res = min(res,dist[j])
            left += B[j]
        upper = A[0]
        for i in range(1,m):
            for j in range(n):
                dist[j] += (2*upper-tot)
                res = min(res,dist[j])  
            upper += A[i]
        return res    