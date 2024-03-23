class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        chars = set(target)
        stickerChars = set(ch for st in stickers for ch in st)
        if not chars<=stickerChars: return -1
        
         #remove unusable stickers and chars to speed up algorithm
        B = []
        for sticker in stickers:
            ctr = Counter(sticker)
            for ch in list(ctr.keys()):
                if ch not in chars:
                    ctr.pop(ch)
            if not ctr: continue #useless sticker omitted
            B.append(ctr)
        
        #remove dominated stickers. In the spirit of greediness, a dominated sticker is always replaceable by its masters
        dominated = set()
        for j in range(len(B)):
            for i in range(j):
                if B[i]<=B[j]: dominated.add(i)
                elif B[i]>B[j]: dominated.add(j)
        B = [B[i] for i in range(len(B)) if i not in dominated]
        
        #BFS
        steps = 0
        wanted = Counter(target)
        visited = set()
        empty = frozenset(Counter().items())
        q = [empty]
        visited.add(empty)
        while q:
            t = []
            for x0 in q:
                x = Counter()
                for k,v in x0:
                    x[k] = v
                for y in B:
                    z = x.copy()
                    for ch in y.keys():
                        if z[ch]==wanted[ch]: continue
                        z[ch] = min(wanted[ch], z[ch]+y[ch])
                    if z==wanted:
                        return 1+steps
                    if z>x:
                        z = frozenset(z.items())
                        if z not in visited:
                            t.append(z)
                            visited.add(z)
            q = t
            steps += 1