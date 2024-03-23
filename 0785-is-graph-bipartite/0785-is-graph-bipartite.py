class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0]*n
        for i in range(n):
            if color[i]==0:
                q = deque()
                q.append(i)
                color[i] = 1
                while q:
                    x = q.popleft()
                    for y in graph[x]:
                        if color[y]==0:
                            q.append(y)
                            color[y] = -color[x]
                        elif color[y]==color[x]:
                            return False
        return True