class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        words.sort(key=lambda x:-len(x))
        intervals = []
        for i in range(len(s)):
            j = -1
            for w in words:
                if s[i:].startswith(w):
                    j = max(j, i+len(w)-1)
                    break
            if j == -1: continue
            elif intervals==[] or intervals[-1][1] < i-1:
                intervals.append([i,j])
            else:
                intervals[-1][1] = max(intervals[-1][1], j)
        buffer = []
        k = 0
        for a,b in intervals:
            buffer.append(s[k:a])
            buffer.append("<b>"+s[a:b+1]+"</b>")
            k = b+1
        buffer.append(s[k:])
        return "".join(buffer)       