class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        D = [int(c) for c in str(n)]
        m = len(D)
        seen = set()
        nonrepeat = sum(perm(10,i)-perm(9,i-1) for i in range(1,m)) #non full digits
        for i,d in enumerate(D):
            for d1 in range(i==0, d):
                if d1 not in seen:
                    nonrepeat += perm(10-i-1,m-i-1)
            if d in seen: break
            seen.add(d)
        
        if len(seen)==m:
            nonrepeat += 1
        return n-nonrepeat