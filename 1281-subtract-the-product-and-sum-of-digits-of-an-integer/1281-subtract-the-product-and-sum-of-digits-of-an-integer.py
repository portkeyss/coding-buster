class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l = [int(i) for i in str(n)]
        prod = 1
        sm = 0
        for i in l:
            prod *= i
            sm += i
        return prod-sm