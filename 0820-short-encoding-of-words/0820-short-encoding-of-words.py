class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        nodes = []
        for w in words:
            t = trie
            for c in w[::-1]:
                t = t[c]
            nodes.append(t)
        return sum(len(w)+1 for i,w in enumerate(words) if len(nodes[i])==0)