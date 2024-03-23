class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(list) #d is the dict for mapping letter list of iterators with current cursor pointing to char
        for w in words:
            it = iter(w)
            d[next(it)].append(it)
        
        res = 0
        for c in s:
            oldBucket = d[c].copy()
            d.pop(c)
            while oldBucket:
                it = oldBucket.pop()
                nxt = next(it, None)
                if nxt:
                    d[nxt].append(it)
                else:
                    res += 1
        return res