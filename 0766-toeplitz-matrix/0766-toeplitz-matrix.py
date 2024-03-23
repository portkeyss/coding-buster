class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m-1):
            for j in range(n-1):
                if matrix[i+1][j+1] != matrix[i][j]:
                    return False
        return True