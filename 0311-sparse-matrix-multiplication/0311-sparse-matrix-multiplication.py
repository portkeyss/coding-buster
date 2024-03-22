class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m = len(A)
        p = len(B)
        n = len(B[0])
        nonzeroA = defaultdict(set)
        for i in range(m):
            for k in range(p):
                if A[i][k] == 0:
                    continue
                nonzeroA[i].add(k)
        nonzeroB = defaultdict(set)
        for j in range(n):
            for k in range(p):
                if B[k][j] == 0:
                    continue
                nonzeroB[j].add(k)
        
        res = [[0]*n for i in range(m)]       
        for i in range(m):
            for j in range(n):
                for k in nonzeroA[i] & nonzeroB[j]:
                    res[i][j] += A[i][k] * B[k][j]
        return res