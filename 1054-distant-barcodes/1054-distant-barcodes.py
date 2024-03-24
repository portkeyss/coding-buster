class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        A = [(-v,k) for k,v in counter.items()]
        heapq.heapify(A)
        res = []
        onHold = None
        while A:
            a,k = heapq.heappop(A)
            res.append(k)
            if onHold:
                heapq.heappush(A,onHold)
                onHold = None
            if a+1<0:
                onHold = (a+1,k)
        return res