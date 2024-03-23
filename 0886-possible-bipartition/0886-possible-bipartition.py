class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n+1)]
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        color = [0]*(n+1)
        
        def dfs(node):
            for x in graph[node]:
                if color[x]==0:
                    color[x] = -color[node]
                    if not dfs(x): return False
                elif color[x]==color[node]:
                    return False
            return True
            
        for i in range(1,n+1):
            if color[i]==0:
                color[i] = 1
                if not dfs(i): return False
        return True