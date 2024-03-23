class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        points.sort()
        n = len(points)
        res = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    a = 0.5*(points[i][1]+points[j][1])*((points[j][0]-points[i][0]))
                    b = 0.5*(points[j][1]+points[k][1])*((points[k][0]-points[j][0]))
                    c = 0.5*(points[i][1]+points[k][1])*((points[k][0]-points[i][0]))
                    res = max(res, abs(a+b-c))
        return res