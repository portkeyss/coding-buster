class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = set(houses)
        heaters = sorted(list(set(heaters)))
        n = len(heaters)
        res = 0
        for house in houses:
            k = bisect.bisect(heaters,house)
            a = heaters[k]-house if k<n else inf
            b = house-heaters[k-1] if k>0 else inf
            res = max(res, min(a, b))
        return res