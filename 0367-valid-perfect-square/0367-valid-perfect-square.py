class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1: return True
        l, r = 2, num//2
        while l<=r:
            m = (l+r)//2
            if m*m==num:
                return True
            elif m*m<num:
                l = m+1
            else:
                r = m-1
        return False