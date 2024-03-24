class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        A = Counter()
        for i in range(m):
            t = []
            s = []
            for j in range(n):
                t.append(str(matrix[i][j]))
                s.append(str(1-matrix[i][j]))
            A["".join(t)] += 1
            A["".join(s)] += 1
        return max(A.values())    