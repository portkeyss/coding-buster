class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        #denary tree
        if k==1: return 1

        def dist(x): #count num the nodes v in subtree of x such that v<=n
            step = 0
            y = x+1
            while x<=n:
                step += min(n+1, y)-x
                x *= 10
                y *= 10
            return step

        k -= 1
        n1 = 1
        while k>0:
            d = dist(n1)
            if d<=k:
                k -= d
                n1 += 1
            else:
                k -= 1
                n1 *= 10
        return n1