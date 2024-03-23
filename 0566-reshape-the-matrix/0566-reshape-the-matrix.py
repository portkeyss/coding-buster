class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        if m*n!=r*c: return mat
        res = [[None]*c for _ in range(r)]
        k = l = 0
        for i in range(m):
            for j in range(n):
                res[k][l] = mat[i][j]
                l += 1
                if l==c:
                    k += 1
                    l = 0
        return res    