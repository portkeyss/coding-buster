class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        x = -inf
        res = -inf
        for j,v in enumerate(values):   
            res = max(res,v-j+x)
            x = max(x,v+j)
        return res