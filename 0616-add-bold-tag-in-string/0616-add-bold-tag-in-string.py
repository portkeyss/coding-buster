class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        dict.sort(key=lambda x:len(x), reverse=True)
        n = len(s)
        boldEnd = [] # end of the longest substring starting from this index found in dict.
        for start in range(n):
            end = -1
            for word in dict:
                if s[start:].startswith(word):
                    end = start + len(word) - 1
                    break
            boldEnd.append(end)
        
        B = [] #intervals of bold intervals
        for start,end in enumerate(boldEnd):
            if end == -1:
                continue
            else:
                if not B or B[-1][1] + 1 < start:
                    B.append([start,end])
                elif B[-1][1] < end:
                    B[-1][1] = end
        if not B:
            return s
        
        buffer = []
        if B[0][0] != 0:
            buffer.append(s[:B[0][0]])
        for i in range(len(B)):
            if i > 0:
                buffer.append(s[B[i-1][1]+1:B[i][0]])
            buffer.append("<b>" + s[B[i][0]:B[i][1]+1] + "</b>")
        if B[-1][1] != n-1:
            buffer.append(s[B[-1][1]+1:])
        return "".join(buffer)     