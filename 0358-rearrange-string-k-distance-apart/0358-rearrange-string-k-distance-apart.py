class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        n = len(s)
        counter = Counter(s)
        validPosition = defaultdict(lambda:0)
        def findChar(x):
            ch = ""
            maxCount = -1
            for c in counter.keys():
                if counter[c]>maxCount and x>=validPosition[c]:
                    maxCount = counter[c]
                    ch = c
            return ch
        buffer = []
        for i in range(n):
            ch = findChar(i) 
            if ch=="": return ""
            buffer.append(ch)
            counter[ch] -= 1
            if counter[ch]==0: counter.pop(ch)
            validPosition[ch]=i+k
        return "".join(buffer) 