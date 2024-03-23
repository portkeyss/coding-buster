class Solution:
    def reverseWords(self, s: str) -> str:
        l = []
        words = s.split()
        for word in words:
            word = list(word)
            word.reverse()
            l.extend(word)
            l.append(' ')
        if l:
            l.pop()
        return "".join(l)