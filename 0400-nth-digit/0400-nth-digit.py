class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 0
        upper = 0
        while upper < n:
            digit += 1
            upper += 9*digit*10**(digit-1)
        lower = (upper-9*digit*10**(digit-1))+1
        num = 10**(digit-1)+(n-lower)//digit
        order = (n-lower)%digit
        return int(str(num)[order])