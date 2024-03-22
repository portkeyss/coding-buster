class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """     
        prev_prev_max_sell = 0
        prev_max_sell = 0
        prev_max_buy = -1<<30
        
        for i in range(len(prices)):
            max_buy = max(prev_max_buy, prev_prev_max_sell - prices[i])
            max_sell = max(prev_max_sell, prev_max_buy + prices[i])
            
            prev_prev_max_sell = prev_max_sell
            prev_max_sell = max_sell
            prev_max_buy = max_buy
            
        return prev_max_sell
        