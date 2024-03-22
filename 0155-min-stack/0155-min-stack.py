class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minVals = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.minVals) == 0 or x <= self.getMin():
            self.minVals.append(x)
        self.stack.append(x)            

    def pop(self):
        """
        :rtype: None
        """
        if self.top() == self.getMin():
            self.minVals.pop()
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minVals[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()