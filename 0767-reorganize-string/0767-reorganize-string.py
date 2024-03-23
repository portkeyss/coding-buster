class Solution:
    def reorganizeString(self, S: str) -> str:
        count = collections.Counter(S)
        orderedCount = [(ct, c) for c, ct in count.items()]
        orderedCount.sort(reverse = True)
        largestCount = orderedCount[0][0]
        if largestCount - 1 > len(S) - largestCount:
            return ""
        
        s = []
        for ct, c in orderedCount:
            s.extend([c]*ct) #s is in the form [aaaaabbbbcccddde] with char count descending
        l = [[] for i in range(largestCount)]
        for i,ch in enumerate(s):#populate them in largestCount segregations
            l[i%largestCount].append(ch)
        p = []
        for m in l:
            p.extend(m)
        return "".join(p)
            