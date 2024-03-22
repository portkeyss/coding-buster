class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.count = 0
        self.size = size
        self.movingFrame = []
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.movingFrame.append(val)
        self.count += 1
        return sum(self.movingFrame[-self.size:])/float(min(self.count, self.size))
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)