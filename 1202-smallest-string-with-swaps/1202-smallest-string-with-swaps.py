class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = defaultdict(lambda:-1)
        rank = Counter()
        def findpar(a):
            if parent[a]==-1:
                return a
            parent[a] = findpar(parent[a])
            return parent[a]
        
        for a,b in pairs:
            x=findpar(a)
            y=findpar(b)
            if x==y: continue
            if rank[x]>rank[y]:
                parent[y]=x
            elif rank[x]<rank[y]:
                parent[x]=y
            else:
                parent[y]=x
                rank[x] += 1
        
        A = defaultdict(list)
        for x in parent:
            A[findpar(x)].append(x)
        bf = list(s)
        for l in A.values():
            l.sort()
            p = list(map(lambda y:s[y], l))
            p.sort()
            for j in range(len(l)):
                bf[l[j]] = p[j]
        return "".join(bf)    