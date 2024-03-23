class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        stack = []
        
        def dfs(p):
            stack.append(p)
            if p == n-1:
                res.append(stack.copy())
            else:
                for m in graph[p]:
                    if m not in stack:
                        dfs(m)
            stack.pop()
        
        dfs(0)
        return res