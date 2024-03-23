class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxSet = set()
        for n in nums:
            maxSet.add(n)
            if len(maxSet) > 3:
                m = min(maxSet)
                maxSet.discard(m)
                    
        return min(maxSet) if len(maxSet) == 3 else max(maxSet)
            