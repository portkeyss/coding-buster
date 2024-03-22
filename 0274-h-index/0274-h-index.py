class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        #we wish to find the largest h value, s.t., count(x>=h) >= h. i.e., count(x>=h)-h >= 0. let f(h) = count(x>=h)-h. It is monotonically nonincreasing functions, which inspires binary search
        left, right = 0, n
        while left < right:
            h = ceil((left+right)/2)
            i = bisect.bisect_left(citations, h)
            if (n-i)-h < 0:
                right = h-1
            else:
                left = h
        return left