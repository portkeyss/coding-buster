class Solution:
    def bitwiseComplement(self, n: int) -> int:
        msk = 1
        i = 0
        while (1<<i)<=n:
            msk |= 1<<i
            i += 1
        return n^msk