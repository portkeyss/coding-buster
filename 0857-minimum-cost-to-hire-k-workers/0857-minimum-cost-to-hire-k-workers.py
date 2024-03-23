class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([float(w)/q,q] for w,q in zip(wage,quality))
        hq = []
        res = inf
        qsum = 0
        for r,q in workers:
            heapq.heappush(hq,-q)
            qsum += q
            if len(hq)>k: 
                largestQ = -heapq.heappop(hq)
                qsum -= largestQ
            if len(hq)==k:
                res = min(res,qsum*r)
        return res