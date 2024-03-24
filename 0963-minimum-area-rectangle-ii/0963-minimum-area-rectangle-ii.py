class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        pointSet = set(tuple(point) for point in points)
        res = math.inf
        for i in range(n):
            for j in range(i+1,n):
                edge1 =(points[j][0]-points[i][0], points[j][1]-points[i][1])
                for k in range(j+1,n):
                    edge2 = (points[k][0]-points[i][0], points[k][1]-points[i][1])
                    if edge1[0]*edge2[0]+edge1[1]*edge2[1]==0:
                        x,y = points[j][0]+points[k][0]-points[i][0], points[j][1]+points[k][1]-points[i][1]
                        if (x,y) in pointSet:
                            res = min(res, sqrt(edge1[0]**2+edge1[1]**2)*sqrt(edge2[0]**2+edge2[1]**2))
        return res if res<math.inf else 0       