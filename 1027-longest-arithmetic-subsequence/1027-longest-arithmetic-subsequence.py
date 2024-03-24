class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        memo = {}
        for j in range(len(A)):
            for i in range(j):
                memo[(A[j] - A[i], j)] = 1 + memo.get((A[j] - A[i], i), 1)
        return max(memo.values())             