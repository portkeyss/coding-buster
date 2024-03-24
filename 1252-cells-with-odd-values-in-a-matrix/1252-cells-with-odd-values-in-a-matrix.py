class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        A = [0]*m
        B = [0]*n
        for r,c in indices:
            A[r] += 1
            B[c] += 1
        return sum((A[i]+B[j])%2==1 for i in range(m) for j in range(n))