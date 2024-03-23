class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        #check a,b,c satisfy the condition: a x b and b x c do not have opposite sign where x is the cross product
        def f(a,b,c):
            return (b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])

        res = True
        flag = 0
        n = len(points)
        points = points+[points[0],points[1]]
        for i in range(n):
            cross = f(points[i],points[i+1],points[i+2])
            if cross==0: continue
            if flag:
                if cross*flag<0: return False
            else:
                flag = cross
        return res