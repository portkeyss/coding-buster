class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        sub = []
        for _,h in envelopes:
            i = bisect.bisect_left(sub,h)
            if i==len(sub):
                sub.append(h)
            else:
                sub[i] = h
        return len(sub)