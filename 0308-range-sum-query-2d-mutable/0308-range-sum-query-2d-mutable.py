class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m, self.n = len(matrix), len(matrix[0])
        self.bit = [[0]*(self.n+1) for _ in range(self.m+1)]
        for i in range(self.m):
            for j in range(self.n):
                self.updateBIT(i+1,j+1,matrix[i][j])
        

    def update(self, row: int, col: int, val: int) -> None:
        oldVal = self.sumRegion(row,col,row,col)
        self.updateBIT(row+1,col+1,val-oldVal)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.queryBIT(row2+1,col2+1)-self.queryBIT(row2+1,col1)-self.queryBIT(row1,col2+1)+self.queryBIT(row1,col1)
        
    def lsb(self, x):
        return x&(-x)
    
    def updateBIT(self, i, j, val):
        r = i
        while r<=self.m:
            c = j
            while c<=self.n:
                self.bit[r][c] += val
                c += self.lsb(c)
            r += self.lsb(r)
    
    def queryBIT(self, i, j):
        sm = 0
        r = i
        while r>0:
            c = j
            while c>0:
                sm += self.bit[r][c]
                c -= self.lsb(c)
            r -= self.lsb(r)
        return sm


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)