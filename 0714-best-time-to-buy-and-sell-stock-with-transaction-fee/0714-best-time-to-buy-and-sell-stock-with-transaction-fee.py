class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        prev_max_buy = -1<<30
        prev_max_sell = 0
        
        for i in range(len(prices)):
            max_buy = max(prev_max_buy, prev_max_sell - prices[i])
            max_sell = max(prev_max_sell, prev_max_buy + prices[i] - fee)
            
            prev_max_buy = max_buy
            prev_max_sell = max_sell
        return prev_max_sell
            
        