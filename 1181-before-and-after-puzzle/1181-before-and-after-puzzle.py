class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        prefix = defaultdict(list)
        suffix = defaultdict(list)
        for i,phrase in enumerate(phrases):
            w = phrase.split(" ")
            prefix[w[0]].append((" ".join(w[1:]),i))
            suffix[w[-1]].append((" ".join(w[:-1]),i))
        M = set()
        for p in suffix:
            for a,i in suffix[p]:
                for b,j in prefix[p]:
                    if i==j: continue
                    x = []
                    if a: x.append(a)
                    x.append(p)
                    if b: x.append(b)
                    if i!=j:
                        M.add(" ".join(x))
        return sorted(list(M))