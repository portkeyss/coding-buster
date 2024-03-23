class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = collections.Counter(words)
        l = list(freq.keys())
        l.sort(key= lambda w: (-freq[w], w))
        return l[:k]