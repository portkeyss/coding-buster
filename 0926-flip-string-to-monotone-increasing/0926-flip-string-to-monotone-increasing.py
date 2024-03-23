class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n = len(S)
        ones = [0]
        for c in S:
            ones.append(ones[-1]+int(c))
        res = inf
        for i in range(n+1):
            res = min(res, 2*ones[i]+n-i-ones[n])
        return res