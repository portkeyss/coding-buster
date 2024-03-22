class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i,x in enumerate(heights):
            while stack and heights[stack[-1]]>=x:
                h = heights[stack.pop()]
                w = i-1-(stack[-1] if stack else -1)
                res = max(res,h*w)
            stack.append(i)
        while stack:
            h = heights[stack.pop()]
            w = len(heights)-1-(stack[-1] if stack else -1)
            res = max(res,h*w)
        return res