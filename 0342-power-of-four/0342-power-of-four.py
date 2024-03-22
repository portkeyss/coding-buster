class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0: return False
        while n>1:
            if n&3==0: n>>=2
            else: return False
        return True