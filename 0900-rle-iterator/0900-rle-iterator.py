class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.cur = 0

    def next(self, n: int) -> int:
        while self.cur < len(self.encoding) and n > 0:
            if self.encoding[self.cur] == 0:
                self.cur += 2
            elif self.encoding[self.cur] == n:
                self.cur += 2
                return self.encoding[self.cur-1]
            elif self.encoding[self.cur] < n:
                n -= self.encoding[self.cur]
                self.cur += 2
            else:
                self.encoding[self.cur] -= n
                return self.encoding[self.cur+1]
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)