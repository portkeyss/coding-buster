class RangeModule:

    def __init__(self):
        self.A = []

    def addRange(self, left: int, right: int) -> None:
        s = []
        i = bisect_left(self.A, left)
        if i%2 == 0: s.append(left)
        j = bisect_right(self.A, right)
        if j%2 == 0: s.append(right)
        self.A[i:j] = s

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect_right(self.A, left)
        j = bisect_left(self.A, right)
        return i==j and i%2

    def removeRange(self, left: int, right: int) -> None:
        s = []
        i = bisect_left(self.A, left)
        if i%2 == 1: s.append(left)
        j = bisect_right(self.A, right)
        if j%2 == 1: s.append(right)
        self.A[i:j] = s



# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)