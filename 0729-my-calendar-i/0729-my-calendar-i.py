class Node(object):    
    __slots__ = 'start', 'end', 'left', 'right'
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
     
    def insert(self, start, end):   
        if start < self.end:    
            if self.start < end:  
                return False
            else:
                if self.left is None:
                    self.left = Node(start, end)
                    return True
                else:
                    return self.left.insert(start, end)
        else: # start >= self.end
            if self.right is None:
                self.right = Node(start, end)
                return True
            else:
                return self.right.insert(start, end)
    
class MyCalendar(object):
    
    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if self.root is None:
            self.root = Node(start, end)
            return True
        else:
            return self.root.insert(start,end)

            
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)