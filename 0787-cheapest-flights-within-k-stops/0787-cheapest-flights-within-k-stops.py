class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = [{} for _ in range(n)]
        for f in flights:
            graph[f[0]][f[1]] = f[2]
        q = deque()
        q.append((src,0))
        price = [[float('inf')]*(K+2) for _ in range(n)]
        price[src][0] = 0
        res = float('inf')
        while q:
            city, step = q.popleft()
            if step == K+1: continue
            for c,p in graph[city].items():
                if price[city][step]+p < price[c][step+1]:
                    price[c][step+1] = price[city][step]+p
                    q.append((c,step+1))   
                    if c == dst: 
                        res = min(res, price[c][step+1])
        return res if res < float('inf') else -1