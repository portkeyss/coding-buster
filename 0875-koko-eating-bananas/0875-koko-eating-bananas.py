class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, sum(piles)
        def totalHours(x):
            return sum(ceil(p/x) for p in piles)
        while l < r:
            mid = (l+r)//2
            if totalHours(mid) > h:
                l = mid+1
            else:
                r = mid
        return l