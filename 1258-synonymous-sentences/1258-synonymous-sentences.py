class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        parent = defaultdict(lambda:-1)
        rank = defaultdict(lambda:0)
        def find(x):
            if parent[x]==-1: return x
            parent[x] = find(parent[x])
            return parent[x]
        for s,t in synonyms:
            x = find(s)
            y = find(t)
            if x==y: continue
            if rank[x]<rank[y]:
                parent[x] = y
            elif rank[x]>rank[y]:
                parent[y] = x
            else:
                parent[y]=x
                rank[x] += 1
        A = parent.keys()
        B = defaultdict(list)
        for u in A:
            B[find(u)].append(u)
        for l in B.values():
            l.sort()
       
        text = text.split(" ")
        n = len(text)
        @lru_cache(None)
        def dfs(p):
            cur = [text[p]] if text[p] not in A else B[find(text[p])]
            if p==n-1: return cur
            l = []
            for x in cur:
                for y in dfs(p+1): 
                    l.append(x+" "+y)
            return l
        return dfs(0)        