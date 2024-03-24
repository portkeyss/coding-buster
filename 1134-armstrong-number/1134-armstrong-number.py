class Solution:
    def isArmstrong(self, N: int) -> bool:
        nlist = [int(n) for n in str(N)]
        k = len(nlist)
        return N == sum(n**k for n in nlist)