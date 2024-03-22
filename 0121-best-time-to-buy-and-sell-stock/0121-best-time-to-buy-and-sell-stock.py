class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_buy = 1<<30
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - min_buy)
            min_buy = min(min_buy, prices[i])
        return max_profit
        