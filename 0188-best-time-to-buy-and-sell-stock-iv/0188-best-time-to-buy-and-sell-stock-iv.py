class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0:
            return 0
        if k >= len(prices)/2:
            mx = 0
            mx_buy = - 1<<30
            for i in range(0,len(prices)):
                prev_mx = mx
                mx = max(mx, mx_buy + prices[i])
                mx_buy = max(mx_buy, prev_mx - prices[i])
            return mx
        
        cur_buy = [-1<<30] * (k + 1)
        cur_sell = [0] + [-1<<30] * k
        for i in range(len(prices)):
            prev_buy = list(cur_buy)
            prev_sell = list(cur_sell)
            for j in range(1,k+1):
                cur_buy[j] = max(prev_buy[j], prev_sell[j-1] - prices[i])
                cur_sell[j] = max(prev_sell[j], prev_buy[j] + prices[i])     
        return max(cur_sell)
        