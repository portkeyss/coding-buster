class StockSpanner(object):

    def __init__(self):
        self.stack = []
        self.idx = -1
        self.stack.append((10**6,self.idx))

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        while self.stack[-1][0] <= price:
            self.stack.pop() 
        self.idx += 1
        count = self.idx - self.stack[-1][1]
        self.stack.append((price, self.idx))
        return count
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)