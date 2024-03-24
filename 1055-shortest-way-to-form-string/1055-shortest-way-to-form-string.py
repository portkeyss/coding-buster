class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s = set(source)
        t = set(target)
        if s&t!=t: return -1
        n = len(source)
        A = [None for _ in range(n+1)]
        A[n] = dict()
        for i in range(n-1,-1,-1):
            A[i] = {k:v for k,v in A[i+1].items()}
            A[i][source[i]] = i
        
        k=n
        res = 0
        for c in target:
            if c not in A[k]:
                k = 0
                res += 1
            k = A[k][c]+1
        return res