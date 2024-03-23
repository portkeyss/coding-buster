class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def innerprod(a, b):
            return a[0]*b[0]+a[1]*b[1]
        def mid(a,b):
            return [(a[0]+b[0])/2, (a[1]+b[1])/2]
        def delta(a,b):
            return [b[0]-a[0], b[1]-a[1]]
        def distsqr(a,b):
            c = delta(a,b)
            return c[0]*c[0]+c[1]*c[1]
        def checkdiagonal(q1,q2,q3,q4): #the advantage of checking diagonal is that the order inside each pair (q1,q2) and (q3,q4) does not matter and we only need to make sure two pairs and orthogonal and midpoint and distsqr are same and nonzero
            d12 = delta(q1, q2)
            d34 = delta(q3, q4)
            return innerprod(d12, d34) == 0 and mid(q1, q2) == mid(q3, q4) and distsqr(q1,q2) == distsqr(q3, q4) > 0
        
        return checkdiagonal(p1,p2,p3,p4) or checkdiagonal(p1,p3,p2,p4) or checkdiagonal(p1,p4,p2,p3)