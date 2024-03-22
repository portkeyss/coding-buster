class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        i1 = i2 = None
        dist = float('inf')
        for i, w in enumerate(words):
            if w == word1:
                if i2 is not None:
                    dist = min(dist, i-i2)
                i1 = i
            elif w == word2:
                if i1 is not None:
                    dist = min(dist, i-i1)
                i2 = i
        return dist         