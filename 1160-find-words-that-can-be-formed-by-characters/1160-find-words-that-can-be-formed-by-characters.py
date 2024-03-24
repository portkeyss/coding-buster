class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charCounts = Counter(chars)
        wordsCount = map(Counter, words)
        res = 0
        for i,wc in enumerate(wordsCount):
            good = all(k in charCounts and v<=charCounts[k] for k,v in wc.items())
            res += len(words[i])*good
        return res