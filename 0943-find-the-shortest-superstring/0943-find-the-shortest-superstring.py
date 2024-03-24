class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        A = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i!=j:
                    for k in range(min(len(words[i]), len(words[j]))-1,0,-1):
                        if words[i][-k:]==words[j][:k]:
                            A[i][j]=k
                            break
        @lru_cache(None)
        def f(prevIdx, mask):
            if mask==((1<<n)-1):return (0,[])
            ans = (inf,[])
            for i in range(n):
                if (1<<i)&mask==0:
                    length,seq = f(i,(1<<i)|mask)
                    l = -A[prevIdx][i]+length if prevIdx>=0 else length
                    if l<ans[0]:
                        ans = l, [i]+seq
            return ans
            
        l,seq = f(-1,0)
        buf = [words[seq[0]]]
        for i in range(1, n):
            k = A[seq[i-1]][seq[i]]
            buf.append(words[seq[i]][k:])
        return "".join(buf)