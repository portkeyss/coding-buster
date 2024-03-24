class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.cb = combinationLength
        self.n = len(characters)
        self.current = None

    def next(self) -> str:
        if self.current is None:
            self.current = [i for i in range(self.cb)]
            return self.characters[:self.cb]
        for i in range(self.cb-1, -1, -1):
            if self.current[i]==self.n-self.cb+i: continue
            self.current[i:] = [j for j in range(self.current[i]+1, self.current[i]+1+self.cb-i)]
            return "".join(self.characters[k] for k in self.current)

    def hasNext(self) -> bool:
        return self.current is None or self.current[0]<self.n-self.cb


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()