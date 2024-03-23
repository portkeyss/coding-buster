class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        B = []
        for i in range(n):
            b = []
            for j in range(m):
                b.append(A[j][i])
            B.append(b)
        return B