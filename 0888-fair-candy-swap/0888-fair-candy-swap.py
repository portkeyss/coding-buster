class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        halfDist = (sum(bobSizes)-sum(aliceSizes))//2
        bob = set(bobSizes)
        for a in aliceSizes:
            b = halfDist+a
            if b in bob:
                return [a, b]