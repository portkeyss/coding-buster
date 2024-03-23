class Trie:
    def __init__(self):
        self.count = 0
        self.children = defaultdict(Trie)
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()  
        for s,t in zip(sentences,times):
            tr = self.trie
            for c in s:
                tr = tr.children[c]
            tr.count = t
        self.cur = self.trie
        self.buffer = []

    def input(self, c: str) -> List[str]:
        if c == "#": 
            self.cur.count += 1 
            self.cur = self.trie
            self.buffer = []
            return []
        self.cur = self.cur.children[c]
        self.buffer.append(c)
        q = deque([(self.cur, "".join(self.buffer))])
        l = []
        while q:
            p, st = q.popleft()
            if p.count > 0:
                l.append((p.count, st))
            for k,v in p.children.items():
                q.append((v, st+k))
        l.sort(key=lambda x: (-x[0], x[1]))
        return [st for _,st in l[:3]]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)