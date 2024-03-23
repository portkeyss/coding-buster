class MagicDictionary:

    def __init__(self):
        self.st = None
        self.A = Counter()

    def buildDict(self, dictionary: List[str]) -> None:
        self.st = set(dictionary)
        for d in dictionary:
            for i in range(len(d)):
                self.A[(d[:i],d[i+1:])] += 1

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            ct = self.A[(searchWord[:i], searchWord[i+1:])]
            if ct==1 and searchWord not in self.st or ct>1: return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)