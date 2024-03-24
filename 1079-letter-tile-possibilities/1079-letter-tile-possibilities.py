class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        factorial =[1,1,2,6,24,120,720,5040]
        counter = Counter(tiles)
        def permRep(freq):
            N = sum(freq)
            return factorial[N]//prod(factorial[i] for i in freq)
        res = 0
        n = len(counter)
        counts = list(counter.values())
        freqs = [[0]*n]
        for j,f in enumerate(counts):
            t = []
            for k in range(1,f+1):
                for freq in freqs:
                    a = freq.copy()
                    a[j] = k
                    res += permRep(a)
                    t.append(a)
            freqs.extend(t)
        return res