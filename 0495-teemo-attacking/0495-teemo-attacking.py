class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        end = -inf
        res = 0
        for t in timeSeries:
            if end>t:
                res -= end-t
            res += duration
            end = t+duration
        return res