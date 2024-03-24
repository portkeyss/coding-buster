class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        words.sort(key=lambda x: len(x))
        for i in range(len(text)):
            for word in words:
                if text[i:].startswith(word):
                    res.append([i,i-1+len(word)])
        return res