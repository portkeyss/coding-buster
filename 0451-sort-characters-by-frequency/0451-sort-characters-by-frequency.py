class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        l = list(freq.items())
        l.sort(key=lambda x:[-x[1],x[0]])
        buffer = []
        for (x,f) in l:
            for _ in range(f):
                buffer.append(x)
        return "".join(buffer)