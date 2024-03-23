class MyCalendarThree(object):

    def __init__(self):
        self.delta = collections.Counter()

    def book(self, start, end):
        self.delta[start] += 1
        self.delta[end] -= 1
        
        ans = active = 0
        for timestamp in sorted(self.delta):
            active += self.delta[timestamp]
            ans = max(ans, active)
        return ans
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)