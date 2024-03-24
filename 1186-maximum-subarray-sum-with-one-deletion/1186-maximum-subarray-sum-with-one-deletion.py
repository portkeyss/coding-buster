class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        x = -inf #max consecutive sum including current number
        y = -inf #max consecutive but one sum including current number, current number may or may not be exluded
        res = -inf
        for a in arr:
            z = max(a+x,a)
            w = max(x, y+a)
            x, y = z, w
            res = max(res, x, y)
        return res    