class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        k = int(sqrt(area))
        while k>0:
            if area%k==0: return [area//k,k]
            k -= 1