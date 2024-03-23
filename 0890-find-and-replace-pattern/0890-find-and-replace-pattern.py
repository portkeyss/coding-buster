class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def translate(w):
            buffer = []
            c = "a"
            dic = {}
            for ch in w:
                if ch not in dic:
                    dic[ch]=c
                    c = chr(ord(c)+1)
                buffer.append(dic[ch])        
            return "".join(buffer)
        p = translate(pattern)
        res = []
        for w in words:
            if translate(w)==p:
                res.append(w)
        return res