class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph = [[set(),set()] for _ in range(n)]
        
        for a,b in red_edges:
            graph[a][0].add(b)
        for a,b in blue_edges:
            graph[a][1].add(b)
        
        q = deque([[0,0],[0,1]])
        dist = [[inf]*2 for _ in range(n)]
        dist[0][0] = dist[0][1] = 0
        while q:
            node,color = q.popleft()
            for nei in graph[node][1-color]:
                if dist[nei][1-color]==inf:
                    dist[nei][1-color]=dist[node][color]+1
                    q.append([nei,1-color])
        res = [-1]*n
        for i in range(n):
            d = min(dist[i])
            if d<inf:
                res[i] = d
        return res