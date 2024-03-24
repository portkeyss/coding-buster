class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        A = [[0]*(1+n) for _ in range(1+m)]
        B = [[0]*(1+n) for _ in range(1+m)]
        k = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                A[i][j] = A[i-1][j]+mat[i-1][j-1]
                B[i][j] = B[i][j-1]+A[i][j]
                while i>=k+1 and j>=k+1 and B[i][j]-B[i-k-1][j]-B[i][j-k-1]+B[i-k-1][j-k-1]<=threshold:
                    k += 1
        return k