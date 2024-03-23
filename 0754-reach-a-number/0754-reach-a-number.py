class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        def findupperbound(t):#find n, s.t. n(n-1)//2 < t <= n(n+1)//2
            l, r = 1, 10**5
            while l < r:
                mid = (l+r)//2
                y = (mid+1)*mid//2
                if y == t:
                    return mid
                elif y < t:
                    l = mid+1
                else:
                    r = mid
            return r
        n=findupperbound(target)
        
        y = (n+1)*n//2
        if y == target or (y-target)%2 == 0:
            return n
        elif (n+1) % 2 == 1:
            return n+1
        else:
            return n+2