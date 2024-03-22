class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """ 
        max_profit = 0
        max_balance_after_buy = - 1<<30
        for i in range(len(prices)):
            prev_max_profit = max_profit
            max_profit = max(max_profit, prices[i] + max_balance_after_buy)
            max_balance_after_buy = max(max_balance_after_buy, prev_max_profit - prices[i])
        return max_profit