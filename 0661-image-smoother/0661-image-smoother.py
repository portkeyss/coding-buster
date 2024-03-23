class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n = len(img),len(img[0])
        A = [[0]*(n+1) for _ in range(m+1)]
        B = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                A[i][j] = A[i-1][j]+img[i-1][j-1]
                B[i][j] = B[i][j-1]+A[i][j]
        for i in range(m):
            for j in range(n):
                a, b, c, d = max(i-1,0), max(j-1,0), min(i+2,m), min(j+2,n)
                img[i][j] = (B[c][d]-B[a][d]-B[c][b]+B[a][b])//((c-a)*(d-b))
        return img