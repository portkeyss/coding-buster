class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x:[-len(x), x])
        nextCharIdx = defaultdict(dict)
        for i in range(len(s)-2, -2, -1):
            nextCharIdx[i] = nextCharIdx[i+1].copy()
            nextCharIdx[i][s[i+1]] = i+1
        for w in dictionary:
            k = -1
            find = True
            for c in w:
                if c in nextCharIdx[k]:
                    k = nextCharIdx[k][c]
                else:
                    find = False
                    break
            if find: return w
        return ""