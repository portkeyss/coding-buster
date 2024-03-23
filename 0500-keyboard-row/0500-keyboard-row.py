class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s = list(map(lambda x: set(c for c in x), ["qwertyuiop", "asdfghjkl", "zxcvbnm"]))
        res = []
        for w in words:
            y = set(c.lower() for c in w)
            for p in s:
                z = y&p
                if z==y:
                    res.append(w)
                    break
                elif z:
                    break
        return res
        