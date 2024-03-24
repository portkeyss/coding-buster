class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        tot = sum(A)
        if tot % 3 != 0:
            return False
        sm = tot // 3
        s = A[0]
        i = 1
        while i < len(A)-2 and s != sm:
            s += A[i]
            i += 1
        if s != sm:
            return False
        s = A[i]
        i += 1
        while i < len(A) - 1 and s != sm:
            s += A[i]
            i += 1
        if s != sm:
            return False     
        return True   