class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mi = 12*60
        times = []
        for timePoint in timePoints:
            h, m = timePoint.split(":")
            times.append(int(h) * 60 + int(m))
        times.sort()
        
        for i in range(1, len(times)):
            a = times[i] - times[i-1]
            b = times[i] - times[0]
            c = min(a, 24*60 - b)
            mi = min(mi, c)
        
        return mi    