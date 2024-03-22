class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0, n-1
        lb, rb = 0,0 #leftBound, rightBound
        res = 0
        while l<=r:
            if lb<rb:
                if height[l]<lb:
                    res += lb-height[l]
                else:
                    lb = height[l]
                l += 1
            else:
                if height[r]<rb:
                    res += rb-height[r]
                else:
                    rb = height[r]
                r -= 1
        return res