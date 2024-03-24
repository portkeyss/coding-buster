class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        t = 0
        ind = {}
        pos = 0
        for i, c in enumerate(keyboard):
            ind[c] = i
        for c in word:
            t += abs(ind[c] - pos)
            pos = ind[c]
        return t    