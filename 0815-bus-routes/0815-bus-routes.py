class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        
        routes = list(map(set,routes))
        buses = defaultdict(set)
        for i,route in enumerate(routes):
            for stop in route:
                buses[stop].add(i)
                
        q = deque()
        dist = dict()
        for b in buses[source]:
            if target in routes[b]: return 1
            q.append(b)
            dist[b] = 1
        while q:
            b = q.popleft()
            for stop in routes[b]:
                for bs in buses[stop]:
                    if bs not in dist:
                        q.append(bs)
                        dist[bs] = dist[b]+1
                        if bs in buses[target]:
                            return dist[bs]
        return -1