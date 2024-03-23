class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        A = [[a,i] for i,(a,_) in enumerate(intervals)]
        A.sort()
        res = []
        for _,e in intervals:
            j = bisect.bisect(A,[e,-1])
            k = A[j][1] if j<n else -1
            res.append(k)
        return res