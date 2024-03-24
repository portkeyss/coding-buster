class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        a, b = toBeRemoved[0], toBeRemoved[1]
        for interval in intervals:
            s, e = interval[0], interval[1]
            if s < a:
                res.append([s, min(e,a)])
            if b < e:
                res.append([max(s,b), e])
        return res