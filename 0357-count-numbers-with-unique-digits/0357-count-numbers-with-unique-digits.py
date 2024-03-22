class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0: return 1
        A = 10
        for i in range(2,n+1):
            A += (9*math.factorial(9)//math.factorial(10-i))
        return A