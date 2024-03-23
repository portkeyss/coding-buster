class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        A = []
        for d,p in zip(difficulty,profit):
            A.append([d,p])
        A.sort(key=lambda x:[x[0],-x[1]])
        B = []
        pred,prep = -inf, -inf
        for d,p in A:
            if d>pred and p>prep:
                B.append([d,p])
                pred,prep = d,p
        n = len(B)
        res = 0
        for w in worker:
            i=bisect.bisect(B,[w])
            if i==n:
                res += B[n-1][1]
            elif B[i][0]==w:
                res += B[i][1]
            elif i>0:
                res += B[i-1][1]
        return res