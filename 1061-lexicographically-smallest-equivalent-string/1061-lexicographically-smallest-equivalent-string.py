class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        parent = dict()
        rank = Counter()
        
        def find(x):
            if x not in parent:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            x = find(x)
            y = find(y)
            if x==y: return
            if rank[x]>rank[y]:
                parent[y] = x
            elif rank[x]<rank[y]:
                parent[x] = y
            else:
                parent[x] = y
                rank[y] += 1
        
        for a,b in zip(A,B):
            union(a,b)

        A = defaultdict(list)
        for c in string.ascii_lowercase:
            A[find(c)].append(c)

        B = dict()
        for x in A:
            A[x].sort()
            for y in A[x]:
                B[y] = A[x][0]
        
        return "".join([B[x] for x in S])