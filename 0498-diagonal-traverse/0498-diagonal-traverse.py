class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # i + j = p,  0 <= i <= m-1, 0 <= j <= n-1 -> max(0,p+1-n) <= i <= min(m-1,p)
        direction = 0
        res = []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        for p in range(m+n-1):
            min_i = max(0, p+1-n)
            max_i = min(m-1, p)
            if direction == 0:
                for i in range(max_i, min_i-1, -1):       
                    res.append(matrix[i][p-i])
            else:
                for i in range(min_i, max_i+1):
                    res.append(matrix[i][p-i])
            direction = 1 - direction
        return res