class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.V = []
        for v in [v1, v2]:
            if v != []:
                self.V.append(v)
        self.i = 0
        self.J = [0] * len(self.V)

    def next(self) -> int:
        ans = self.V[self.i][self.J[self.i]]
        self.J[self.i] += 1
        if self.J[self.i] == len(self.V[self.i]):
            del self.V[self.i]
            del self.J[self.i]
            self.i = self.i % len(self.V) if len(self.V) > 0 else 0
        else:
            self.i = (self.i + 1) % len(self.V)
        return ans

    def hasNext(self) -> bool:
        return len(self.V) > 0

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())