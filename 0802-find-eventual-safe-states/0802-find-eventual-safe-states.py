class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        A = [0]*n
        def dfs(node):
            if A[node]==0:
                if not graph[node]:
                    A[node]=1
                else:
                    A[node]=2#temperary
                    for nei in graph[node]:
                        if dfs(nei) in [-1,2]:
                            A[node]=-1
                            break
                    if A[node]==2:
                        A[node] = 1
            return A[node]
        
        res = []
        for i in range(n):
            if dfs(i)==1: res.append(i)
        return res