class StringIterator:

    def __init__(self, compressedString: str):
        self.count = deque()
        curCount = 0
        for c in compressedString:
            if c.isalpha():
                if self.count:
                    self.count[-1].append(curCount)
                curCount = 0
                self.count.append([c])
            else:
                curCount = 10*curCount + int(c)
        if self.count:
            self.count[-1].append(curCount)

    def next(self) -> str:
        if self.count:
            if self.count[0][1] > 1:
                self.count[0][1] -= 1
                return self.count[0][0]
            else:
                return self.count.popleft()[0]
        else:
            return " "

    def hasNext(self) -> bool:
        return len(self.count) > 0
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()