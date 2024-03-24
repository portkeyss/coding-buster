class Trie:
    def __init__(self):
        self.isEnd = False
        self.children = defaultdict(Trie)
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            t = self.trie
            for ch in word:
                t = t.children[ch]
            t.isEnd = True
        self.prev = [self.trie]
        
    def query(self, letter: str) -> bool:
        res = False
        cur = []
        for a in self.prev:
            if letter in a.children:
                x = a.children[letter]
                cur.append(x)
                if x.isEnd:
                    res = True
        cur.append(self.trie)        
        self.prev = cur
        return res

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)