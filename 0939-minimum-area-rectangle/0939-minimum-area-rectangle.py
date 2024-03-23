class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        visited = set()
        res = math.inf
        for a, b in points:
            for c, d in visited:
                if a != c and b != d and (a, d) in visited and (c, b) in visited:
                    res = min(res, abs(a-c)*abs(b-d))
            visited.add((a,b))
        return res if res < math.inf else 0