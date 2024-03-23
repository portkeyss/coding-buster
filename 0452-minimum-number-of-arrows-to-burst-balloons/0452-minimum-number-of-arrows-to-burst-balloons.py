class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        front = float('-inf')
        ans = 0
        for p0,p1 in points:
            if p0 > front:
                front = p1
                ans += 1
        return ans