class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if m>n: m,n = n,m
        def f(x):
            count = 0
            for i in range(1,m+1):
                count += min(x//i,n)
                if count>=k: return True
            return False
        
        l, r = 1, m*n
        while l<r:
            mid = (l+r)//2
            if f(mid):
                r = mid
            else:
                l = mid+1
        return l