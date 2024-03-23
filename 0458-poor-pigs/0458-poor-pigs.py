class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        s = minutesToTest//minutesToDie+1
        p = 0
        while s**p<buckets:
            p += 1
        return p