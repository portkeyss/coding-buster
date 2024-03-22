class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #a is max profit for at most one transaction, b is max profit for at most two trans
        a = b = 0
        #c is max net money flow after one purchase, d is the max net money flow after at most two purchases
        c = d = -inf
        for p in prices:
            b = max(b,d+p,a)
            d = max(d,a-p,c)
            a = max(a,c+p,0)
            c = max(c,-p)
        return b