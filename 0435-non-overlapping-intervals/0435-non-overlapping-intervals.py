class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        front = float('-inf')
        ans = 0
        for s,e in intervals:
            if s < front:
                ans += 1
            else:
                front = e
        return ans