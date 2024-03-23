class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = [[] for _ in range(n+1)]
        for p in times:
            edges[p[0]].append((p[1],p[2]))
        dist = [float('inf')]*(n+1)
        
        hq = []
        dist[k] = 0
        heapq.heappush(hq, (dist[k],k))
        
        while hq:
            curDist, u = heapq.heappop(hq)
            if curDist > dist[u]:
                continue
            for v,w in edges[u]:
                if dist[v] > curDist+w:
                    dist[v] = curDist+w
                    heapq.heappush(hq, (dist[v],v))
        delay = max(dist[1:])
        return delay if delay < float('inf') else -1