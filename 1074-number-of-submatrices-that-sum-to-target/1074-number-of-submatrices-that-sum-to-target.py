class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        prefixByCol = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                prefixByCol[i+1][j+1] = prefixByCol[i][j+1]+matrix[i][j]
        
        res = 0
        for i in range(1,m+1):
            for j in range(i):
                x = 0
                counter = Counter()
                counter[0] = 1
                for k in range(n):
                    x += prefixByCol[i][k+1]-prefixByCol[j][k+1]
                    res += counter[x-target]
                    counter[x] += 1
        return res