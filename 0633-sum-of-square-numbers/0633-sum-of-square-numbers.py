class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x = 0
        while x*x*2<=c:
            y = int(sqrt(c-x*x))
            if x*x+y*y==c: return True
            x += 1
        return False