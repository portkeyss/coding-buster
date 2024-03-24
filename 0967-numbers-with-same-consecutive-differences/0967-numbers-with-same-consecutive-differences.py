class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        dp = list(i for i in range(10))
        for bit in range(2,n+1):
            t = []
            for a in dp:
                d = a//(10**(bit-2))
                if d+k<10:
                    t.append((d+k)*(10**(bit-1))+a)
                if d-k>=0 and k>0:
                    t.append((d-k)*(10**(bit-1))+a)
            dp = t
        return list(j for j in dp if j>=10**(n-1))