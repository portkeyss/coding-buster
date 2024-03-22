class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v = v
        self.i = 0
        self.j = 0
        while self.i < len(self.v) and self.v[self.i] == []:
            self.i += 1

    def next(self) -> int:
        res = self.v[self.i][self.j]
        self.j += 1
        while self.i < len(self.v) and self.j == len(self.v[self.i]):
            self.i += 1
            self.j = 0
        return res

    def hasNext(self) -> bool:
        return self.i < len(self.v)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()