class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        #longest path in directed acyclic graph (DAG)
        neis = [[] for _ in range(n+1)]
        for a,b in relations:
            neis[a].append(b)
        
        A = dict()
        
        def dfs(node):
            if node in A: return A[node]
            if not neis[node]:
                A[node] = 1
                return 1
            A[node]=-1
            for x in neis[node]:
                depth = dfs(x)
                if depth==-1:
                    return -1
                A[node] = max(A[node], 1+depth)
            return A[node]

        res = 0
        for i in range(1,n+1):
            t = dfs(i)
            if t==-1: return -1
            res = max(res,t)
        
        return res