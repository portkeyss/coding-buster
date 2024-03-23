class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        mat = [[1]*n for _ in range(n)]
        for i,j in mines:
            mat[i][j] = 0
        A = [[0]*(n+1) for _ in range(n+1)]
        B = [[0]*(n+2) for _ in range(n+1)]
        C = [[0]*(n+1) for _ in range(n+1)]
        D = [[0]*(n+1) for _ in range(n+2)]
        for i in range(n):
            for j in range(n):
                A[i+1][j+1] = A[i+1][j]+1 if mat[i][j]==1 else 0
            for j in range(n-1,-1,-1):
                B[i+1][j+1] = B[i+1][j+2]+1 if mat[i][j]==1 else 0
        for j in range(n):
            for i in range(n):
                C[i+1][j+1] = C[i][j+1]+1 if mat[i][j]==1 else 0
            for i in range(n-1,-1,-1):
                D[i+1][j+1] = D[i+2][j+1]+1 if mat[i][j]==1 else 0
        
        res = 0
        for i in range(n):
            for j in range(n):
                res = max(res, min(A[i+1][j+1], B[i+1][j+1], C[i+1][j+1], D[i+1][j+1])) 
        return res