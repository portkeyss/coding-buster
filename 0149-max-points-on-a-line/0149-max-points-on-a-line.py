class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n==1: return 1
        A = defaultdict(set)
        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1,n):
                x2, y2 = points[j][0], points[j][1]
                key = None
                if x1==x2:
                    key = (1,0,x1)
                if y1==y2:
                    key = (0,1,y1)
                else:
                    w = math.gcd(abs(y2-y1),abs(x2-x1))
                    a,b = (y2-y1)//w, (x2-x1)//w
                    key = (a,b,-a*x1+b*y1)
                A[key].add(i)
                A[key].add(j)
        return max(len(x) for x in A.values())