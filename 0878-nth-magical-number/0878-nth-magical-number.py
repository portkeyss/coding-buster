class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        LCM = lcm(a,b)
        def magicBelow(x):
            return x//a+x//b-x//LCM
        l, r = min(a,b), n*min(a,b)
        while l<r:
            m = (l+r)//2
            if magicBelow(m)<n:
                l = m+1
            else:
                r = m
        return l%(10**9+7) 