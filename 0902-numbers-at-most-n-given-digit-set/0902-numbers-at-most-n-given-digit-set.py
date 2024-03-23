class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        m = len(digits)
        N = str(n)
        bit = len(N)
        
        unfilled = 0
        for b in range(1,bit):
            unfilled += pow(m,b)
        
        def filled(curBit):
            if curBit==bit: return 1
            ans = 0
            for d in digits:
                if d<N[curBit]:
                    ans += pow(m,bit-curBit-1)
                elif d==N[curBit]:
                    ans += filled(curBit+1)
                else:
                    break
            return ans
        
        return unfilled+filled(0)