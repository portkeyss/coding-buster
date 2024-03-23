class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        # x,y are to be the second largest and largest element in S
        x, y = -inf, -inf
        res = 0
        #greedily add element at the end of the current interval
        for a, b in intervals:
            if not a<=x<y<=b:
                if y<b:
                    x = y
                    y = b
                    res += 1
                if not a<=x:
                    x = b-1
                    res += 1
        return res