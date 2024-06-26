class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        x0,y0,x1,y1 = coordinates[0][0], coordinates[0][1],coordinates[1][0], coordinates[1][1]
        return all((y-y0)*(x1-x0)==(x-x0)*(y1-y0) for x,y in coordinates)