class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append((target,0))
        pq = []
        fuel = startFuel
        prev = 0
        res = 0
        for loc,f in stations:
            fuel -= loc-prev
            while fuel<0 and pq:
                fuel+=-heapq.heappop(pq)
                res += 1
            if fuel<0: return -1
            prev = loc
            heapq.heappush(pq, -f)
        return res