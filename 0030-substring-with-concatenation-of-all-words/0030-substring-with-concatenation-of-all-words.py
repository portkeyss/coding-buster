class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m,n = len(words),len(words[0])
        counter = Counter(words)
        res = []
        for start in range(n):
            A = Counter()
            tally = 0
            for j in range(start+n-1,len(s),n):
                if j-n*(m+1)+1>=0:
                    p = s[j-n*(m+1)+1:j-n*m+1]
                    A[p] -= 1
                    if p in counter and A[p]==counter[p]-1: tally -= 1
                t = s[j-n+1:j+1]
                A[t] += 1
                if t in counter and A[t]==counter[t]:  tally += 1
                if tally==len(counter):
                    res.append(j-n*m+1)
        return res  