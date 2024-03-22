class Solution:
    def getSum(self, a: int, b: int) -> int:
        def add(m,n):
            if m&n: return add(m^n, (m&n)<<1)
            return m^n
            
        def subtract(m,n):
            if ~m&n: return subtract(m^n, (~m&n)<<1)
            return m^n
            
        if a < 0 and b < 0: return -add(-a, -b)
        if -a >= b > 0: return -subtract(-a, b)
        elif b > -a > 0: return subtract(b, -a)
        elif -b >= a > 0: return -subtract(-b, a)
        elif a > -b > 0: return subtract(a, -b)
        else: return add(a, b)
        