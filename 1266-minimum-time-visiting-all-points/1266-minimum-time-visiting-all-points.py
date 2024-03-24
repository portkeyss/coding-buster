class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        for i in range(1,n):
            stepX, stepY = abs(points[i][0]-points[i-1][0]), abs(points[i][1]-points[i-1][1])          
            res += max(stepX, stepY)
        return res  