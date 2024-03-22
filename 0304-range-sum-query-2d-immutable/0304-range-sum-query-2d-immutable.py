class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        prefixByCol = [[0]*(n+1) for _ in range(m+1)]
        self.cumSum = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                prefixByCol[i][j] = prefixByCol[i-1][j] + matrix[i-1][j-1]
                self.cumSum[i][j] = self.cumSum[i][j-1] + prefixByCol[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.cumSum[row2+1][col2+1] - self.cumSum[row1][col2+1] - self.cumSum[row2+1][col1] + self.cumSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)