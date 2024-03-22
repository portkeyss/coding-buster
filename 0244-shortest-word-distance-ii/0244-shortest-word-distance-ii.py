class WordDistance:

    def __init__(self, words: List[str]):
        self.wordindices = defaultdict(list)
        for i, word in enumerate(words):
            self.wordindices[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        l1 = self.wordindices[word1]
        l2 = self.wordindices[word2]
        dist = float('inf')
        i = j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                dist = min(dist, l2[j] - l1[i])
                i += 1
            else:
                dist = min(dist, l1[i] - l2[j])
                j += 1
        return dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)