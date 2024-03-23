class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n==1: return "".join([str(i) for i in range(k)])
        @lru_cache(None)
        def constructNodes(m):
            if m==0: return [""]
            res = []
            for i in range(k):
                for c in constructNodes(m-1):
                    res.append(str(i)+c)
            return res
        
        out = dict()
        nodes = constructNodes(n-1)
        
        for u in nodes:
            out[u]=[]
            for x in range(k):
                v = u[1:]+str(x)
                out[u].append(v)
                
        start = "".join(["0"]*(n-1))
        epath = [] #euler path
        cpath = [start] #current path
        while cpath:
            u = cpath[-1]
            if out[u]:
                v = out[u].pop()
                cpath.append(v)
            else:
                epath.append(u)
                cpath.pop()
        
        buffer = [start[:-1]]
        while epath:
            x = epath.pop()
            buffer.append(x[-1])
        return "".join(buffer)