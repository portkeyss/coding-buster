class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        A = dict()
        for a,b in intervals:
            if a not in A or A[a]<b:
                A[a] = b
        starts = sorted(list(A.keys()))
        prev = -inf
        res = 0
        for a in starts:
            if A[a]>prev:
                res += 1
                prev = A[a]
        return res