class WordFilter:

    def __init__(self, words: List[str]):
        self.A = dict()
        for i,w in enumerate(words):
            n = len(w)
            for p in range(1,n+1):
                pre = w[:p]
                for q in range(n):
                    suf = w[q:]
                    self.A[(pre,suf)]=i
                    
    def f(self, prefix: str, suffix: str) -> int:
        if (prefix,suffix) in self.A:
            return self.A[(prefix,suffix)]
        else:
            return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)